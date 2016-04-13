from Base_job import BaseJob
import requests


class FacebookJob(BaseJob):

    def get_socialMetrics(self):
        payload = {"q": 'SELECT like_count,total_count,share_count,click_count,comment_count FROM link_stat WHERE url = "{url}"'.format(url = self.url)}
        r = requests.get('http://graph.facebook.com/fql',verify = False, params = payload)
        data = r.json()
        return data
