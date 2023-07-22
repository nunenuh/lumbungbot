from .api import basic
from .utils import Handlers

api_handlers = Handlers()
api_handlers.add(basic.handlers)
