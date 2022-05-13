import webapp2

class MainPage(webapp2.RequestHandler):
     def get(self):
         num =5
         for i in range(1,11):
             ans = num*i
             self.response.write(str(num)+"X"+str(i)+"="+str(ans)+"<br>")
        
app = webapp2.WSGIApplication([('/',MainPage),], debug=True)