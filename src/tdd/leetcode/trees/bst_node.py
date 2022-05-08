from inspect import currentframe
from typing import Any, Optional, Union


class BSTNode(object):
    def __init__(self, data, parent=None) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent

    def insert(self, value: Any) -> bool:
        current = self
        while current is not None:
            self.parent = current
            if value < current.data:
                current = current.leftChild
            elif value > current.data:
                current = current.rightChild
            else:
                print(f"ENTRY FAILED: {str(value)} already exists. Entries must be unique.")
                return False

        if value < self.parent.data:
            self.parent.leftChild = BSTNode(data=value, parent=self.parent)
        elif value > self.parent.data:
            self.parent.rightChild = BSTNode(data=value, parent=self.parent)
        return True

    def insert_recursive(self, value: Any) -> Union[None, bool]:
        if value == self.data:
            print(f"ENTRY FAILED: {str(value)} already exists. Entries must be unique.")
            return False
        elif value < self.data:
            if self.leftChild:
                self.leftChild.insert_recursive(value)
            else:
                self.leftChild = BSTNode(data=value, parent=self)
                return True
        else:
            if self.rightChild:
                self.rightChild.insert_recursive(value)
            else:
                self.rightChild = BSTNode(data=value, parent=self)
                return True

    def search(self, target: Any) -> Union["BSTNode", bool, None]:
        current = self
        while current is not None:
            if target == current.data:
                return current
            elif target < current.data:
                current = current.leftChild
            else:
                current = current.rightChild
        return False

    def search_recursive(self, target: Any) -> Union["BSTNode", bool]:
        if target == self.data:
            return self
        elif target < self.data:
            if self.leftChild:
                return self.leftChild.search_recursive(target=target)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.search_recursive(target=target)
            else:
                return False

    def delete(self, target: Any) -> Union["BSTNode", bool, None]:
        if target < self.data:
            if self.leftChild:
                self.leftChild = self.leftChild.delete(target=target)
            else:
                print(f"{str(target)} NOT FOUND")
                return None

        elif target > self.data:
            if self.rightChild:
                self.rightChild = self.rightChild.delete(target=target)
            else:
                print(f"{str(target)} NOT FOUND")
                return None
        else:
            if self.leftChild is None and self.rightChild is None:
                self = None
                return None
            elif self.leftChild is None:
                tmp = self.rightChild
                self = None
                return tmp
            elif self.rightChild is None:
                tmp = self.leftChild
                self = None
                return tmp
            else:
                current = self.rightChild
                while (current.leftChild is not None):
                    current = current.leftChild
                self.data = current.data
                self.rightChild = self.rightChild.delete(target=current.data)
        return self


