import ConfigParser

import requests

from twisted.application import internet
from twisted.web import server
from twisted.web.resource import Resource
from twisted.python import usage


class TargetsResource(Resource):
    isLeaf = True

    def __init__(self, targets={}):
        #super(TargetsResource, self).__init__()
        self.targets = targets

    def render_GET(self, request):
        if self.targets:
            responses = {}
            for t, options in self.targets.items():
                url = options['url']
                resp = requests.get(url)
                responses[url] = resp.status_code
            return '<ul>%s</ul>' % '\n'.join(['<li>%s - %s</li>' % (url, status)
                for url, status in responses.items()])
        return "<h1>No targets</h1>"


class Options(usage.Options):
    optParameters = (
        ("port", "p", 8080, "The port number to listen on."),
        ("targets", "t", None, "The file with targets to monitoring."),
        )


def makeService(config):
    port = int(config['port'])

    targets = {}
    targets_config = config.get('targets')
    if targets_config:
        parser = ConfigParser.ConfigParser()
        parser.read([targets_config])
        for section in parser.sections():
            if parser.has_option(section, 'url'):
                targets[section] = {'url': parser.get(section, 'url')}

    site = server.Site(TargetsResource(targets))
    return internet.TCPServer(port, site)