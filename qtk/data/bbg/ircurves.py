"""
This file handles Interest Rate Curves
"""
import blpapi
from .defs import SECURITY_DATA, FIELD_DATA, CURVE_MEMBERS

def get_ircurve_members_request_handler(index_ticker):
    def request_handler(refservice):
        request = refservice.createRequest("ReferenceDataRequest")
        request.append("securities", index_ticker)
        request.append("fields", "CURVE_MEMBERS")
        return request
    return request_handler


def ircurve_members_event_handler(event, output):
    event_type = event.eventType()
    if (event_type == blpapi.Event.RESPONSE) or (event_type == blpapi.Event.PARTIAL_RESPONSE):
        for msg in event:
            field_data = msg.getElement(SECURITY_DATA).getValueAsElement(0).getElement(FIELD_DATA)

            curve_members = field_data.getElement(CURVE_MEMBERS)
            member_tickers = [curve_members.getValueAsElement(i).getElementAsString("Curve Members")
                              for i in range(curve_members.numValues())]
            output["tickers"] = member_tickers



