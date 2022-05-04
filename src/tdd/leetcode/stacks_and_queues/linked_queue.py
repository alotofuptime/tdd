from dataclasses import dataclass
from typing import Generator, Optional, Any, Iterable


class LinkedQueue(object):

    @dataclass
    class QueueNode(object):
        data: Any = None
        nxt: Optional["LinkedQueue.QueueNode"] = None

    def __init__(self, front=None):
        self.__front = self.new_node(front) if front else front
        self.__rear = self.__front if front else None
        self.__size = 1 if front else 0

    def __repr__(self) -> str:
        queue_str = " -> ".join([str(node.data) for node in self])
        queue_str += " -> None"
        return queue_str

    def __iter__(self) -> Generator:
        curr = self.__front
        while curr:
            yield curr
            curr = curr.nxt

    def __len__(self) -> int:
        return self.__size

    @property
    def front(self):
        return self.__front

    @property
    def rear(self):
        return self.__rear

    @property
    def size(self):
        return self.__size

    @classmethod
    def new_node(cls, value: Any) -> QueueNode:
        if isinstance(value, LinkedQueue.QueueNode):
            return value
        else:
            return cls.QueueNode(value)

    def is_empty(self) -> bool:
        return True if not self.__front else False

    def enqueue(self, value: Any) -> None:
        new_node = self.new_node(value)
        if self.is_empty():
            self.__rear = self.__front = new_node
        else:
            self.__rear.nxt = new_node
            self.__rear = self.__rear.nxt
        self.__size += 1

    def enqueue_all(self, values: Iterable) -> None:
        for value in values:
            self.enqueue(value)

    def dequeue(self) -> Optional[QueueNode]:
        node = self.__front
        if not self.is_empty():
            self.__front = self.__front.nxt
            self.__size -= 1
        return node

    def peek(self) -> Optional[QueueNode]:
        return self.__front

