import os
import json
import urllib
import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
	def get(self):
		path = os.path.join(os.path.dirname(__file__), "index.html")
		context = {}
		self.response.out.write(template.render(path, context))

	def post(self):
		longitude = self.request.get("longitude")	
		latitude = self.request.get("latitude")
		url = "https://api.open-meteo.com/v1/forecast?latitude="+latitude+ "&longitude=" + longitude+ "&hourly=temperature_2m"
		data = urllib.urlopen(url).read()
		data = json.loads(data)
		if(data['hourly']['temperature_2m'][0]):
			temp = data['hourly']['temperature_2m'][0]
			
			template_values = {
					"temperature": temp
			}
			path = os.path.join(os.path.dirname(__file__), 'results.html')
			self.response.out.write(template.render(path, template_values))
		else:
			path = os.path.join(os.path.dirname(__file__), "error.html")
			context = {}
			self.response.out.write(template.render(path, context))
		
        
        
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)