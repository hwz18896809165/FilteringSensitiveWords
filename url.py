from handlers.index import IndexHandler
from handlers.index import SearchHandler
url = [
    (r'/', IndexHandler),
    (r'/search',SearchHandler)
]