from qtk.data.bbg.requesthandler import BlpapiRequestHandler
from qtk.data.bbg.ircurves import get_ircurve_members_request_handler, ircurve_members_event_handler
import logging


consoleHandler = logging.StreamHandler()
logger = logging.getLogger()
logger.addHandler(consoleHandler)

blp = BlpapiRequestHandler()
request_handler = get_ircurve_members_request_handler("YCGT0025 Index")

with blp:
    output = blp.send_request(request_handler, ircurve_members_event_handler)

print output