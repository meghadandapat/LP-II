import webapp2

class MainPage(webapp2.RequestHandler):
     def get(self):
          def recur_fibo(n):
                if n <= 1:
                     return n
                else:
                    return(recur_fibo(n-1) + recur_fibo(n-2))

          nterms = 8
          if nterms <= 0:
                self.response.write("Plese enter a positive integer")
          else:
                self.response.write("Fibonacci sequence upto 8 numbers : ")
                for i in range(nterms):
                     self.response.write(recur_fibo(i))
        
app = webapp2.WSGIApplication([('/',MainPage),], debug=True)