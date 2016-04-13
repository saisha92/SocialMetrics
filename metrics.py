import falcon
from Jobs.pinterest_job import PinterestJob
from Jobs.stumbleupon_job import StumbleUponJob
from Jobs.facebook_job import FacebookJob
from Jobs.linkedin_job import LinkedInJob
import json

class MetricResource(object):

    def on_get(self,req,resp,url):
    	url = "http://"+url
    	Metrics = {}
    	stumbleUponJob = StumbleUponJob(url)
    	pinterestJob = PinterestJob(url)
    	facebookJob = FacebookJob(url)
    	linkedinJob = LinkedInJob(url)
    	Metrics["Stumble_Upon"] = stumbleUponJob.data
    	Metrics["Pinterest"] = pinterestJob.data
    	Metrics["Facebook"] = facebookJob.data
    	Metrics["LinkedIn"] = linkedinJob.data
    	#resp.body = '{"message": "Hello world!"}'
        resp.body = json.dumps(Metrics)
        resp.status = falcon.HTTP_200

