from typing import Optional, Any, Generator, Iterable

class LinkedList:

    class ListNode:
        def __init__(self, data):
            self.__data = data
            self.__next = None

        def __repr__(self) -> str:
            return f"Node({self.__data})"

        @property
        def data(self) -> Any:
            return self.__data

        #TODO handle set data as node obj edge case. do we want that to be allowed?
        @data.setter
        def data(self, data: Any) -> None:
            self.__data = data

        @property
        def next(self) -> Any:
            return self.__next

        @next.setter
        def next(self, data) -> None:
            self.__next = LinkedList.new_node(data) if (data is not None) else None

    def __init__(self, head=None):
        self.__head = self.new_node(head) if (head is not None) else head
        self.__tail = head
        self.__size = 0 if head is None else 1

    def __repr__(self) -> str:
        return " -> ".join([str(node.data) for node in self])

    def __contains__(self, key: Any) -> bool:
        return self.search(key)

    def __iter__(self) -> Generator:
        curr = self.__head
        while curr:
            yield curr
            curr = curr.next

    def __getitem__(self, idx: int) -> ListNode:
        return self.get_nth(idx)

    def __setitem__(self, idx: int, data: Any) -> None:
        return self.update(idx, data)

    def __len__(self):
        return self.__size

    @property
    def head(self) -> ListNode:
        return self.__head

    @head.setter
    def head(self, data: Any) -> None:
        return self.prepend(data)

    @property
    def tail(self) -> ListNode:
        return self.__tail

    @tail.setter
    def tail(self, data: Any) -> None:
        return self.append(data)

    @property
    def size(self) -> int:
        return self.__size

    @classmethod
    def new_node(cls, data: Any) -> Optional[ListNode]:
        new_node = data if isinstance(data, cls.ListNode) else cls.ListNode(data)
        return new_node

    def is_empty(self) -> bool:
        return True if not self.__head else False

    def append(self, data: Any) -> None:
        new_node = self.new_node(data)
        if self.is_empty():
            self.__tail = self.__head = new_node
            self.__size += 1
            return

        curr = self.__head
        while curr.next:
            curr = curr.next
        curr.next = self.__tail = new_node
        self.__size += 1

    def append_all(self, sequence: Iterable) -> None:
        try:
            for item in sequence:
                self.append(item)
        except TypeError as err:
            raise err("sequence must be iterable(e.g., list, tuple")

    def prepend(self, data: Any) -> None:
        new_node = self.new_node(data)
        if self.is_empty():
            self.__head = self.__tail = new_node
            self.__size += 1
            return

        new_node.next = self.__head
        self.__head = new_node
        self.__size += 1

    def insert_nth(self, data: Any, idx: int) -> None:
        try:
            self[idx]
        except IndexError as err:
            raise err("Index out of range")
        except TypeError as err:
            raise err("idx must be of type int")

        if idx == 0:
            return self.prepend(data)

        # TODO handle -1 idx edge case
        # [1, 2, 3, 4, 5]
        # [-5, -4, -3, -2, -1]
        # is -1 indexing worth the trouble for this specific method?
        new_node, prev = self.new_node(data), None
        curr, pos = self.__head, 0
        while pos != idx:
            prev = curr
            curr = curr.next
            pos += 1
        prev.next, new_node.next = (new_node, curr)
        self.__size += 1

    def delete_head(self) -> None:
        if self.is_empty():
            return
        if self.__head.next:
            self.__head = self.head.next
        else:
            self.__head, self.__tail = (None, None)
        self.__size -= 1

    def delete_tail(self) -> None:
        if self.is_empty():
            return
        if self.__tail is self.__head:
            return self.delete_head()

        curr, prev = (self.__head, None)
        while (curr and curr != self.__tail):
            prev, curr = (curr, curr.next)
        self.__tail, prev.next = (prev, None)
        self.__size -= 1

    def delete_nth(self, idx: int) -> None:
        try:
            self[idx]
        except TypeError:
            raise TypeError("idx must be of type int")
        if idx >= self.size:
            raise IndexError("Index out of range")
        if idx == 0 :
            return self.delete_head()
        if idx == (self.size - 1):
            return self.delete_tail()

        curr, prev = self.__head, None
        pos = 0
        while (curr and pos != idx):
            prev, curr = curr, curr.next
            pos += 1
        prev.next, curr = curr.next, None
        self.__size -= 1

    def get_nth(self, idx: int) -> Optional[ListNode]:
        if not isinstance(idx, int):
            raise TypeError("idx must be of type int")
        if idx >= self.__size:
            raise IndexError("Index out of range")
        if idx == -1:
            return self.__tail

        curr, pos = self.__head, 0
        while pos != idx:
            curr = curr.next
            pos += 1
        return curr

    def search(self, key: Any) -> bool:
        if self.is_empty():
            return False

        curr = self.__head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False

    def reverse(self) -> None:
        if self.is_empty():
            return

        curr, prev = self.__head, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.__head = prev

    def update(self, idx: int, data: Any) -> None:
        try:
            self[idx]
        except TypeError as err:
            raise err("idx must be of type int")
        except IndexError as err:
            raise err("Index out of range")
        if self.is_empty():
            return
        if idx == -1:
            self.__tail.data = data
            return

        curr, pos = self.__head, 0
        while pos != idx:
            curr = curr.next
            pos += 1
        curr.data = data

