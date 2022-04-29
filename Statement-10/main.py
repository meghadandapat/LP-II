import os
import json
import urllib
import webapp2
from google.appengine.ext.webapp import template
class MainPage(webapp2.RequestHandler):
    def get(self):
        context = {}
        path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
        self.response.out.write(template.render(path, context))
    def post(self):
        uniName = self.request.get('uniName')
        url = "http://universities.hipolabs.com/search?name="+ uniName
        data = urllib.urlopen(url).read()
        data = json.loads(data)
       
        name = data[0]['name'] or "not available"
        country = data[0]['country'] or "not available"
        domain = data[0]['domains'][0] or "not available"
        webpage = data[0]['web_pages'][0] or "not available"
        
        context = {
            "name": name,
             "country": country,
             "domain":domain,
             "webpage":webpage
        }

        path = os.path.join(os.path.dirname(__file__), 'templates/results.html')
        self.response.out.write(template.render(path, context))   
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)