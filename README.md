# SocialMetrics

This helps us to fetching the social reach of a particular website. This app is built out using the Falcon framework https://github.com/falconry/falcon. The social reach a particular website has gives a clear indication of the popularity of the website. I've struggled with finding the various social metrics and making separate API calls to Facebook, Pinterest, LinkedIn and Stumble Upon is time consuming, so I built out this app so that you make a single request and you get back the Social metric in the form of a JSON. The App follows REST architectural style and is intended to make life easier for developers.

# Making the Call

To access the data type this in your address bar http://morning-bastion-61876.herokuapp.com/metrics/ {your Url} . So lets say for example you want to know about the reach of Google. Your request would look like http://morning-bastion-61876.herokuapp.com/metrics/www.google.com . Make sure your url is just www.your-site.com ,please avoid giving the entire url like http://www.your-site.com. This App is deployed in Heroku and has an uptime of 18 hours in a 24 hour period. So if for some reason you are unable to access the data for your site please check back after 6 hours.


