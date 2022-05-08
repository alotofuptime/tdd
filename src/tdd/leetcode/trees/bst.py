from typing import Any, Optional

from tdd.leetcode.trees.bst_node import BSTNode


class BinarySearchTree(object):
    def __init__(self, root=None) -> None:
        self.__root = root

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, node: BSTNode):
        self.__root = node

    def insert(self, value: Any) -> Optional[bool]:
        if self.__root:
            return self.__root.insert(value)
        else:
            self.__root = BSTNode(data=value, parent=self.__root)
            return True

    def insert_recursive(self, value: Any) -> Optional[bool]:
        if self.__root:
            return self.__root.insert_recursive(value)
        else:
            self.__root = BSTNode(data=value, parent=self.__root)
            return True

    def search(self, value: Any) -> Optional[bool]:
        if self.__root:
            return self.__root.search(target=value)
        else:
            return False

    def search_recursive(self, value: Any) -> Optional[bool]:
        if self.__root:
            return self.__root.search_recursive(target=value)
        else:
            return False

    def delete(self, value: Any) -> Optional[bool]:
        if self.__root is not None:
            self.__root = self.root.delete(target=value)



