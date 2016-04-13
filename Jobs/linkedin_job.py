from Base_job import BaseJob
import requests
import json

class LinkedInJob(BaseJob):

    def get_socialMetrics(self):
        payload = {"url": self.url, "format": "json"}
        r = requests.get('http://www.linkedin.com/countserv/count/share',params = payload)
        data = r.json()
        return data

