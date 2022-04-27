from dataclasses import dataclass
from typing import Any, Optional

@dataclass
class TreeNode(object):
    value: Any = None
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None

class BinaryTree(object):
    def __init__(self, root=None):
        self.root = TreeNode(root) if root else root

    def pre_order(self, start: TreeNode, trav_str="") -> str:
        if start:
            trav_str += f"{start.value} - "
            trav_str = self.pre_order(start.left, trav_str)
            trav_str = self.pre_order(start.right, trav_str)
        return trav_str

    def in_order(self, start: TreeNode, trav_str="") -> str:
        if start:
            trav_str = self.in_order(start.left, trav_str)
            trav_str += f"{start.value} - "
            trav_str = self.in_order(start.right, trav_str)
        return trav_str

    def post_order(self, start: TreeNode, trav_str="") -> str:
        if start:
            trav_str = self.post_order(start.left, trav_str)
            trav_str = self.post_order(start.right, trav_str)
            trav_str += f"{start.value} - "
        return trav_str



def pre_order_dfs(node: TreeNode) -> None:
    if not node:
        return
    print(node.value)

    pre_order_dfs(node.left)
    pre_order_dfs(node.right)
