from twisted.application.service import ServiceMaker
 
Sample = ServiceMaker(
    "HttpMon",
    "httpmon.tap",
    "Http Monitoring",
    "httpmon"
)