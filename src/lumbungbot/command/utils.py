from typing import Dict, List

from telegram.ext import CommandHandler


class Handlers:
    def __init__(self) -> None:
        self.data = []

    def add(self, handler_dict: Dict):
        hlist = self._build_list(handler_dict)
        self.data.append(hlist)

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

        return dlist
