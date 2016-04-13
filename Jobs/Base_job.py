
"""
Base Job so that other Social API's can inherit from this Base class
"""


class BaseJob(object):

    def __init__(self, url):
        self.url = url
        self.data = self.get_socialMetrics()

    def get_socialMetrics(self):
        raise NotImplementedError