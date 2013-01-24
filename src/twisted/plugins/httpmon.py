from twisted.application.service import ServiceMaker
 
Sample = ServiceMaker(
    "HttpMon",
    "httpmon.tap",
    "A Http Monitoring Web Server.",
    "httpmon"
)