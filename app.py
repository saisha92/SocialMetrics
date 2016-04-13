import falcon
import metrics

api = application = falcon.API()

metrics = metrics.MetricResource()

api.add_route('/metrics/{url}',metrics)