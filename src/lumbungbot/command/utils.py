from typing import Dict, List

from telegram.ext import CommandHandler, BaseHandler


class Handlers:
    def __init__(self) -> None:
        self.data = []

    def add(self, handler_dict: Dict):
        hlist = self._build_list(handler_dict)
        self.data.append(hlist)
        
    def add_handler(self, handler: BaseHandler):
        self.data.append([handler])

    def _build_list(self, handler_dict: Dict):
        list_handler: List = []
        for key, value in handler_dict.items():
            handler = CommandHandler(key, value)
            list_handler.append(handler)

        return list_handler
    

    def get_list(self):
        dlist = []
        for hlist in self.data:
            dlist.extend(hlist)
        
        print(dlist)
        return dlist
