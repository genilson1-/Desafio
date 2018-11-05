import tornado
from tornado.web import RequestHandler, Application
from tornado_http_auth import BasicAuthMixin, auth_required
from tornado.ioloop import IOLoop
credentials = {'user1': 'pass1'}


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")


class MainHandler(BaseHandler, BasicAuthMixin):
    @auth_required(realm='Protected', auth_func=credentials.get)
    @tornado.web.authenticated
    def get(self):
        if not self._current_user:
            self.redirect("/login")
        name = tornado.escape.xhtml_escape(self._current_user)
        self.write("Hello, " + name)

class TestHandler(BaseHandler, tornado.web.RequestHandler):
    @tornado.web.authenticated 
    def get(self):
        self.write('foif')


class LoginHandler(BaseHandler, BasicAuthMixin):
    @auth_required(realm='Protected', auth_func=credentials.get)
    def get(self):
        return(self.set_secure_cookie("user", self._current_user))
       # self.post()
        #self.write('<html><body><form action="/login" method="post">'
         #          'Name: <input type="text" name="name">'
          #         '<input type="submit" value="Sign in">'
           #        '</form></body></html>')
    #def post(self):
     #   self.set_secure_cookie("user", self.get_argument("name"))
      #  self.redirect("/")

#class Application(tornado.web.Application):
#    def __init__(self):
#        handlers = [
#            (r"/", MainHandler),
#            (r"/login", LoginHandler),
#           ]
#        cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__"


settings = {
"cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
"login_url": "/login",
}

def main():

    # Verify the database exists and has the correct layout
    app = tornado.web.Application([
        (r"/", MainHandler),
        (r"/login", LoginHandler),
        (r"/teste", TestHandler),
],  **settings)

    #app = Application()
    app.listen(8888)
    IOLoop.current().start()

if __name__ == "__main__":
    main()
