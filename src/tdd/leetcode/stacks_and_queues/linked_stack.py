from typing import Any, Optional
from attr import dataclass


class LinkedStack(object):
    @dataclass
    class StackNode(object):
        data: Any = None
        nxt: Optional["LinkedStack.StackNode"] = None

    def __init__(self, top=None) -> None:
        self.top = top
        self.bottom = top if top else None
        self.size = 1 if top else 0

    @classmethod
    def new_node(cls, data):
        if isinstance(data, LinkedStack.StackNode):
            return data
        return cls.StackNode(data)
