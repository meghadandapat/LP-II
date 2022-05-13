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
        temp = self.request.get('zipCode')

        country = temp[0].upper()+temp[1:].lower()
        url = "https://covid-api.mmediagroup.fr/v1/cases?country=" + country
 

        data = urllib.urlopen(url).read()
        data = json.loads(data)
     
        population = data['All']['population']
        confirmed = data['All']['confirmed']
        deaths = data['All']['deaths']
        capital=data['All']['capital_city']

        template_values = {
            'country': country,
            'population':population,
            'confirmed':confirmed,
            'deaths':deaths,
            'capital':capital
        }
        path = os.path.join(os.path.dirname(__file__), 'results.html')
        self.response.out.write(template.render(path, template_values))
        
        
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)