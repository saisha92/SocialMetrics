from Base_job import BaseJob
import requests
import re
import json


class PinterestJob(BaseJob):

    def get_socialMetrics(self):
        data = {}
        payload = {"url": self.url}
        r = requests.get('http://api.pinterest.com/v1/urls/count.json', params=payload)
        regex = re.compile(r'"count":(\d+)')
        result = re.search(regex, r.content)
        if result:
            value = result.group(1)
            data["value"] = value
        #json_data = json.dumps(data)
        return data
