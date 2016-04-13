from Base_job import BaseJob
import requests
import json

class StumbleUponJob(BaseJob):
    
    def get_socialMetrics(self):
        data = {}
        payload = {"url": self.url}
        r = requests.get('http://www.stumbleupon.com/services/1.01/badge.getinfo', params=payload)
        content = r.json()
        if 'views' in content['result']:
            data["value"] = content['result']['views']
        else:
            data["value"] = 0    
        #json_data = json.dumps(data)
        return data