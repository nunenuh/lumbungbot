from .api import basic
from .api import mentions
from .utils import Handlers

api_handlers = Handlers()
api_handlers.add(basic.handlers)
api_handlers.add_handler(mentions.message_handler)
