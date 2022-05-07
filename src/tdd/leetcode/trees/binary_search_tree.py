import math
from typing import Any, Optional
from attr import dataclass


class BinarySearchTree(object):
    @dataclass
    class BSTNode(object):
        data: Any = None
        left: Optional["BinarySearchTree.BSTNode"] = None
        right: Optional["BinarySearchTree.BSTNode"] = None
        parent: Optional["BinarySearchTree.BSTNode"] = None

    def __init__(self, root=None) -> None:
        self.root = root

    def insert(self, data: Any) -> None:
        if self.root is None:
            self.root = self.BSTNode(data)
        else:
            return self.__insert(self.root, data)

    def __insert(self, node: BSTNode, data: Any) -> None:
        """Private insert helper function"""

        if node.data < data:
            if node.right is None:
                node.right = self.BSTNode(data, parent=node)
            else:
                self.__insert(node.right, data)
        elif node.data > data:
            if node.left is None:
                node.left = self.BSTNode(data, parent=node)
            else:
                self.__insert(node.left, data)
        else:
            return

    def search(self, data: Any) -> Optional[Any]:
        def __search(node: Optional[BinarySearchTree.BSTNode], data: Any) -> Optional[Any]:
            """Private search helper function"""

            if node is None:
                return False
            if node.data == data:
                return node.data

            try:
                if node.data < data:
                    return __search(node.right, data)
                if node.data > data:
                    return __search(node.left, data)
            except TypeError:
                return False

        return __search(self.root, data)

    def update(self, target: Any, data: Any) -> bool:
        def __update(node: Optional[BinarySearchTree.BSTNode], target: Any, data: Any):
            if node is None:
                return False
            if node.data == target:
                node.data = data
                return True

            if node.data < target:
                return __update(node.right, target, data)
            if node.data > target:
                return __update(node.left, target, data)

        return __update(self.root, target, data)

    def delete(self, target: Any) -> Optional[None]:
        def __delete(node: BinarySearchTree.BSTNode, target: Any):
            if (target < node.data):
                if node.left:
                    node.left = __delete(node.left, target)
                else:
                    print(str(target), "not found in tree")
            elif (target > node.data):
                if node.right:
                    node.right = __delete(node.right, target)
                else:
                    print(str(target), "not found in tree")
            else:
                if node.left is None and node.right is None:
                    node = None
                    return None
                elif node.left is None:
                    tmp = node.right
                    node = None
                    return tmp
                elif node.right is None:
                    tmp = node.left
                    node = None
                    return tmp
                else:
                    curr = node.right
                    while curr.left is not None:
                        curr = curr.left
                    node.data = curr.data
                    node.right = __delete(node.right, curr.data)

        if self.root is not None:
            self.root = __delete(self.root, target)

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
