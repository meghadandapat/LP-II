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
        ShowName = self.request.get('ShowName')
        url = "http://api.tvmaze.com/search/shows?q="+ ShowName
        data = urllib.urlopen(url).read()
        data = json.loads(data)
       
        name = data[0]['show']['name'] or "not available"
        language = data[0]['show']['language'] or "not available"
        genres = data[0]['show']['genres'][0] or "not available"
        officialSite = data[0]['show']['officialSite'] or "not available"
        image = data[0]['show']['image']['original'] or "not available"
        summary = data[0]['show']['summary'] or "not available"
        rating = data[0]['show']['rating']['average'] or "not available"
        context = {
            "name": name,
            "language":language,
            "genres" : genres,
            "officialSite" : officialSite,
            "image" : image,
            "summary" : summary,
            "rating" : rating
        }
        path = os.path.join(os.path.dirname(__file__), 'templates/results.html')
        self.response.out.write(template.render(path, context))   
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)