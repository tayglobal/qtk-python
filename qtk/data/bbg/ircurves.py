"""
This file handles Interest Rate Curves
"""
import blpapi
from .defs import BLP_SECURITY_DATA, BLP_FIELD_DATA, BLP_CURVE_MEMBERS, BLP_SECURITY
from .mapper import bbg_to_std, fmt
from .. import fields as fl

_CURVE_MEMBER_DATA0 = ["CPN", "CPN_FREQ", "ISSUE_DT", "MATURITY",
                       "DAY_CNT_DES", "PX_LAST", "SECURITY_TYP", "SECURITY_TYP2",
                       "BPIPE_REFERENCE_SECURITY_CLASS"]


def get_ircurve_members_request_handler(index_ticker, curve_date):
    def request_handler(session):
        refservice = session.getService("//blp/refdata")
        request = refservice.createRequest("ReferenceDataRequest")
        request.append("securities", index_ticker)
        request.append("fields", "CURVE_MEMBERS")
        overrides = request.getElement("overrides")
        override_field = overrides.appendElement()
        override_field.setElement("fieldId","CURVE_DATE")
        override_field.setElement("value", curve_date.strftime("%Y%m%d"))
        return request
    return request_handler


def ircurve_members_event_handler(event, output):
    event_type = event.eventType()
    if (event_type == blpapi.Event.RESPONSE) or (event_type == blpapi.Event.PARTIAL_RESPONSE):
        for msg in event:
            field_data = msg.getElement(BLP_SECURITY_DATA).getValueAsElement(0).getElement(BLP_FIELD_DATA)

            curve_members = field_data.getElement(BLP_CURVE_MEMBERS)

            member_tickers = [{fl.SECURITY_ID.id: curve_members.getValueAsElement(i).getElementAsString("Curve Members")}
                              for i in range(curve_members.numValues())]
            output[fl.CURVE_MEMBERS.id] = member_tickers


def get_ircurve_member_data_request_handler(curve_members, asof_date):
    def request_handler(session):
        refservice = session.getService("//blp/refdata")
        #request = refservice.createRequest("HistoricalDataRequest")
        request = refservice.createRequest("ReferenceDataRequest")
        for c in curve_members:
            request.append("securities", c[fl.SECURITY_ID.id])

        for field in _CURVE_MEMBER_DATA0:
            request.append("fields", field)
        dt = asof_date.strftime("%Y%m%d")
        #request.set("startDate", dt)
        #request.set("endDate", dt)
        return request
    return request_handler


def ircurve_members_data_event_handler(event, output):
    event_type = event.eventType()
    curve_members = output[fl.CURVE_MEMBERS.id]
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
                for f in _CURVE_MEMBER_DATA0:
                    key, val = fmt(field_data, f)
                    data_dict[key.id] = val
