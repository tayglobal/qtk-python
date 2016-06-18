"""
This file handles Interest Rate Curves
"""
import blpapi

from .defs import BLP_SECURITY_DATA, BLP_FIELD_DATA, BLP_CURVE_MEMBERS, BLP_SECURITY
from .mapper import fmt, get_instrument
from qtk.fields import Field as fl
from qtk.converters import QuantLibConverter as qlf
from qtk import Template


class IRCurveData(object):
    _CURVE_MEMBER_DATA0 = ["CPN", "CPN_FREQ", "ISSUE_DT", "MATURITY",
                           "DAY_CNT_DES"]
    _CURVE_MEMBER_DATA1 = ["SECURITY_TYP", "SECURITY_TYP2", "BPIPE_REFERENCE_SECURITY_CLASS"]

    def __init__(self, blp_request_handler):
        self._blp = blp_request_handler

    def get_curve_members(self, index_ticker, curve_date):
        bbg_date = qlf.to_date_yyyymmdd(curve_date)

        # make all the required requests
        request_handler = self._get_ircurve_members_request_handler(index_ticker, bbg_date)
        output = self._blp.send_request(request_handler, self._ircurve_members_event_handler)
        request_handler = self._get_ircurve_member_data_request_handler(output[fl.INSTRUMENT_COLLECTION.id])
        output = self._blp.send_request(request_handler, self._ircurve_members_data_event_handler, output=output)
        request_handler = self._get_hist_price_request_handler(output[fl.INSTRUMENT_COLLECTION.id], bbg_date)
        output = self._blp.send_request(request_handler, self._hist_price_event_handler, output=output)

        output[fl.ASOF_DATE.id] = curve_date
        output[fl.DATA_SOURCE.id] = "BBG-BLPAPI"
        output[fl.TEMPLATE.id] = Template.TS_YIELD_BOND.id
        return output

    @staticmethod
    def _get_ircurve_members_request_handler(index_ticker, curve_date):
        def request_handler(session):
            refservice = session.getService("//blp/refdata")
            request = refservice.createRequest("ReferenceDataRequest")
            request.append("securities", index_ticker)
            request.append("fields", "CURVE_MEMBERS")
            overrides = request.getElement("overrides")
            override_field = overrides.appendElement()
            override_field.setElement("fieldId","CURVE_DATE")
            override_field.setElement("value", curve_date)
            return request
        return request_handler

    @staticmethod
    def _ircurve_members_event_handler(event, output):
        event_type = event.eventType()
        if (event_type == blpapi.Event.RESPONSE) or (event_type == blpapi.Event.PARTIAL_RESPONSE):
            for msg in event:
                field_data = msg.getElement(BLP_SECURITY_DATA).getValueAsElement(0).getElement(BLP_FIELD_DATA)

                curve_members = field_data.getElement(BLP_CURVE_MEMBERS)

                member_tickers = [{fl.SECURITY_ID.id: curve_members.getValueAsElement(i).getElementAsString("Curve Members")}
                                  for i in range(curve_members.numValues())]
                output[fl.INSTRUMENT_COLLECTION.id] = member_tickers

    @classmethod
    def _get_ircurve_member_data_request_handler(cls, curve_members):
        def request_handler(session):
            refservice = session.getService("//blp/refdata")
            #request = refservice.createRequest("HistoricalDataRequest")
            request = refservice.createRequest("ReferenceDataRequest")
            for c in curve_members:
                request.append("securities", c[fl.SECURITY_ID.id])

            for field in cls._CURVE_MEMBER_DATA0+cls._CURVE_MEMBER_DATA1:
                request.append("fields", field)
            return request
        return request_handler

    @classmethod
    def _ircurve_members_data_event_handler(cls, event, output):
        event_type = event.eventType()
        curve_members = output[fl.INSTRUMENT_COLLECTION.id]
        if (event_type == blpapi.Event.RESPONSE) or (event_type == blpapi.Event.PARTIAL_RESPONSE):
            for msg in event:
                security_data = msg.getElement(BLP_SECURITY_DATA)

                for i in range(security_data.numValues()):
                    element = security_data.getValueAsElement(i)
                    seq_no = element.getElementAsInteger("sequenceNumber")
                    security = element.getElementAsString(BLP_SECURITY)
                    field_data = element.getElement(BLP_FIELD_DATA)
                    data_dict = curve_members[seq_no]
                    assert(security == data_dict[fl.SECURITY_ID.id])
                    for f in cls._CURVE_MEMBER_DATA0:
                        key, val = fmt(field_data, f)
                        data_dict[key.id] = val
                    key, asset_type = fmt(field_data, "BPIPE_REFERENCE_SECURITY_CLASS")
                    key, security_type = fmt(field_data, "SECURITY_TYP")
                    key, security_subtype = fmt(field_data, "SECURITY_TYP2")
                    instrument = get_instrument(asset_type, security_type, security_subtype)
                    data_dict[fl.TEMPLATE.id] = instrument.id


    @classmethod
    def _get_hist_price_request_handler(cls, curve_members, curve_date):
        def request_handler(session):
            refservice = session.getService("//blp/refdata")
            request = refservice.createRequest("HistoricalDataRequest")
            for c in curve_members:
                request.append("securities", c[fl.SECURITY_ID.id])
            request.set("startDate", curve_date)
            request.set("endDate", curve_date)
            request.append("fields", "PX_MID")
            return request
        return request_handler

    @classmethod
    def _hist_price_event_handler(cls, event, output):
        event_type = event.eventType()
        curve_members = output[fl.INSTRUMENT_COLLECTION.id]
        if (event_type == blpapi.Event.RESPONSE) or (event_type == blpapi.Event.PARTIAL_RESPONSE):
            for i,msg in enumerate(event):
                security_data = msg.getElement(BLP_SECURITY_DATA)
                security = security_data.getElementAsString(BLP_SECURITY)
                field_data = security_data.getElement(BLP_FIELD_DATA).getValueAsElement(0)
                seq_no = security_data.getElementAsInteger("sequenceNumber")
                data_dict = curve_members[seq_no]
                assert(security == data_dict[fl.SECURITY_ID.id])

                for f in ["PX_MID", "date"]:
                    key, val = fmt(field_data, f)
                    data_dict[key.id] = val