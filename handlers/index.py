import tornado.web
from tornado.websocket import WebSocketHandler
import json
import os
import sys
current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_dir)
sys.path.append("..")
from sensitive_word_filtration_project import start_search,start_create_dictionaryTree
start_create_dictionaryTree()

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class SearchHandler(tornado.web.RequestHandler):
    def get(self):
        keywords = self.get_argument('keywords')
        self.write(json.dumps(start_search(keywords)))