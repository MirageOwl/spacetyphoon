import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("view/base.html")
