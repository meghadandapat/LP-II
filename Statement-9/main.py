import json
import urllib
import webapp2
class MainPage(webapp2.RequestHandler):
    def get(self):
        url = "https://ghibliapi.herokuapp.com/films"
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        ans = []
        for i in data:
            ans.append(i['title'])
        self.response.write("<h3>Ghibli movies to watch</h3>")
        for i in range(len(ans)):
            self.response.write(ans[i]+"<br>")   
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)