import math
from typing import Any, Optional
from attr import dataclass


class BinarySearchTree(object):
    @dataclass
    class BSTNode(object):
        data: Any = None
        left: Optional["BinarySearchTree.BSTNode"] = None
        right: Optional["BinarySearchTree.BSTNode"] = None

    def __init__(self, root=None) -> None:
        self.root = root

    def insert(self, data: Any) -> None:
        if self.root is None:
            self.root = self.BSTNode(data)
        else:
            return self.__insert(self.root, data)

    def __insert(self, node: BSTNode, data: Any) -> None:
        if node.data < data:
            if node.right is None:
                node.right = self.BSTNode(data)
            else:
                self.__insert(node.right, data)
        elif node.data > data:
            if node.left is None:
                node.left = self.BSTNode(data)
            else:
                self.__insert(node.left, data)
        else:
            return

    def search(self, data: Any) -> Optional[Any]:
        return self.__search(self.root, data)

    def __search(self, node: BSTNode, data: Any) -> Optional[Any]:
        if node is None:
            return False
        if node.data == data:
            return node.data

        #TODO handle edge case where node.data & data entered by user are of different types
        # (i.e., node.data is 9 but user searches for "Nine")
        if node.data < data:
            return self.__search(node.right, data)
        if node.data > data:
            return self.__search(node.left, data)

    def is_bst(self):
        def __is_bst(node, left=float("-inf"), right=float("inf")) -> bool:
            if node is None:
                return True

            if isinstance(node.data, str):
                left, right = (-math.inf, math.inf)
                if (ord(node.data[0]) < left) and (ord(node.data[0]) > right):
                    return False
            else:
                if (node.data < left) and (node.data > right):
                    return False

            return (__is_bst(node.right, node.data, right) and
                    __is_bst(node.left, left, node.data))

        return __is_bst(self.root)

    def dfs_inorder(self, node: Optional[BSTNode]) -> list:
        if node is None:
            return []

        return self.dfs_inorder(node.left) + [node.data] +  self.dfs_inorder(node.right)
