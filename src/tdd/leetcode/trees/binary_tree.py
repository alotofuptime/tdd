from dataclasses import dataclass
from typing import Any, Optional
from tdd.leetcode.stacks_and_queues.linked_queue import LinkedQueue

@dataclass
class TreeNode(object):
    value: Any = None
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None

class BinaryTree(object):
    def __init__(self, root=None):
        self.root = TreeNode(root) if root else root

    def pre_order(self, start: Optional[TreeNode], trav_str="") -> str:
        if start:
            trav_str += f"{start.value} - "
            trav_str = self.pre_order(start.left, trav_str)
            trav_str = self.pre_order(start.right, trav_str)
        return trav_str

    def in_order(self, start: Optional[TreeNode], trav_str="") -> str:
        if start:
            trav_str = self.in_order(start.left, trav_str)
            trav_str += f"{start.value} - "
            trav_str = self.in_order(start.right, trav_str)
        return trav_str

    def post_order(self, start: Optional[TreeNode], trav_str="") -> str:
        if start:
            trav_str = self.post_order(start.left, trav_str)
            trav_str = self.post_order(start.right, trav_str)
            trav_str += f"{start.value} - "
        return trav_str

    def level_order(self, start: TreeNode) -> Optional[str]:
        if start is None:
            return

        queue = LinkedQueue()
        queue.enqueue(start)

        trav_str = ""
        while len(queue) > 0:
            trav_str += f"{queue.peek().data.value}" + " - "
            next_node = queue.dequeue()

            if next_node.data.left:
                queue.enqueue(next_node.data.left)
            if next_node.data.right:
                queue.enqueue(next_node.data.right)
        return trav_str


def pre_order_dfs(node: Optional[TreeNode]) -> None:
    if not node:
        return
    print(node.value)

    pre_order_dfs(node.left)
    pre_order_dfs(node.right)
