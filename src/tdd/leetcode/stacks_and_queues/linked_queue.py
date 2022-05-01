from dataclasses import dataclass
from typing import Optional, Any, Iterable

#@dataclass
#class QueueNode(object):
#    data: Any = 0
#    nxt: Optional["QueueNode"] = None


class LinkedQueue(object):

    @dataclass
    class QueueNode(object):
        data: Any = 0
        nxt: Optional["QueueNode"] = None

    def __init__(self, front=None):
        self.front = self.new_node(front) if front else front
        self.rear = self.front if front else None
        self.size = 1 if front else 0

    @classmethod
    def new_node(cls, value: Any) -> QueueNode:
        if isinstance(value, LinkedQueue.QueueNode):
            return value
        else:
            return cls.QueueNode(value)

    def is_empty(self) -> bool:
        return True if not self.front else False

    def enqueue(self, value: QueueNode) -> None:
        new_node = self.new_node(value)
        if self.is_empty():
            self.rear = self.front = new_node

        curr = self.front
        while curr.nxt:
            curr = curr.nxt
            curr.nxt = self.rear = new_node
        self.size += 1

    def enqueue_all(self, values: Iterable) -> None:
        for value in values:
            self.enqueue(value)
