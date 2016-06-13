from qtk.data.bbg.requesthandler import BlpapiRequestHandler
from qtk.data.bbg.ircurves import IRCurveData
import logging
import datetime
import QuantLib as ql


consoleHandler = logging.StreamHandler()
logger = logging.getLogger()
logger.addHandler(consoleHandler)

blp = BlpapiRequestHandler()
blp.start_session()
date = datetime.date(2016, 6, 9)

ircurve_data = IRCurveData(blp)
output = ircurve_data.get_curve_members("YCGT0025 Index", date)

print output

blp.stop_session()

