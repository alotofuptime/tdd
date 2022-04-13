class LinkedList:

    class ListNode:
        def __init__(self, data):
            self.__data = data
            self.__next = None

        def __repr__(self):
            return f"Node({self.__data})"

        # what if user wanted to set/update data of node?
        @property
        def data(self):
            return self.__data

        @property
        def next(self):
            return self.__next

        @next.setter
        def next(self, data) -> None:
            self.__next = LinkedList.new_node(data)

    def __init__(self, head=None):
        self.__head = self.new_node(head) if head is not None else head
        self.__tail = head
        self.__size = 0 if head is None else 1

    def __repr__(self):
        return " -> ".join([str(node.data) for node in self])

    def __iter__(self):
        curr = self.__head
        while curr:
            yield curr
            curr = curr.next

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, data):
        return self.prepend(data)

    @property
    def tail(self):
        return self.__tail

    @tail.setter
    def tail(self, data: ListNode) -> None:
        return self.append(data)

    @property
    def size(self):
        return self.__size

    @classmethod
    def new_node(cls, data):
        new_node = data if isinstance(data, cls.ListNode) else cls.ListNode(data)
        return new_node

    def is_empty(self):
        return True if not self.__head else False

    def append(self, data):
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

    def prepend(self, data):
        new_node = self.new_node(data)
        if self.is_empty():
            self.__head = self.__tail = new_node
            self.__size += 1
            return

        new_node.next = self.__head
        self.__head = new_node
        self.__size += 1
