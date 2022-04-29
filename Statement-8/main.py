import os
import json
import urllib
import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        city_name = self.request.get('zipCode')
        api_key = "6fed8996a96c98b705eaa03c8befa332"
        base_url="https://api.openweathermap.org/data/2.5/weather?"
        url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        print(data)
        template_values = {
            "Weather_Description": data['weather'][0]['description'],
            "Temp_feels_like":data['main']['feels_like'],
            "humididty":data['main']['humidity'],
            "wind_speed":data["wind"]['speed'],
            "visibility":data["visibility"]
        }
        path = os.path.join(os.path.dirname(__file__), 'results.html')
        self.response.out.write(template.render(path, template_values))
        
        
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)