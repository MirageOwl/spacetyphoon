import os
import random
from handler import *

def make_app():
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "cookie_secret": str(random.getrandbits(16)),
        "login_url": "/login"
    }
    return tornado.web.Application([
        (r"/", MainHandler)],
        **settings)
