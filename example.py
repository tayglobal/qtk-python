from qtk.data.bbg.requesthandler import BlpapiRequestHandler
from qtk.data.bbg.ircurves import get_ircurve_members_request_handler, ircurve_members_event_handler,\
    get_ircurve_member_data_request_handler, ircurve_members_data_event_handler
import logging
import datetime

consoleHandler = logging.StreamHandler()
logger = logging.getLogger()
logger.addHandler(consoleHandler)

blp = BlpapiRequestHandler()
blp.start_session()

date = datetime.date(2016, 6, 3)
request_handler = get_ircurve_members_request_handler("YCGT0025 Index", date)

output = blp.send_request(request_handler, ircurve_members_event_handler)
print output

print "Tickers"
for t in output["tickers"]:
    print t
request_handler = get_ircurve_member_data_request_handler(output["tickers"], date)

output = blp.send_request(request_handler, ircurve_members_data_event_handler)
print output

blp.stop_session()