import tornado.web
from helper import *

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("view/base.html")

class ItemHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("view/make_item.html")

    def post(self):
        name = self.get_argument("item-name")
        desc = self.get_argument("item-desc")
        price = self.get_argument("price")
        img_url = self.get_argument("img-url")
        add_item(name, desc, price, img_url)
        self.write({"name": name})
