from dataclasses import dataclass
from typing import Any, Optional
from collections import deque
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

    #TODO FIX BUG NOT PROPERLY GETTING SUM OF EACH LEVEL SHOULD ONLY BE 3 INTEGERS IN SUM OF LEVLS
    def bfs_sum(self, start: TreeNode) -> Optional[list[int]]:
        if start is None:
            return []

        queue = deque()
        queue.append(start)

        sum_of_levels = []
        sum_of_levels.append(start.value)
        total = 0
        while len(queue) > 0:
            next_node = queue.popleft()
            if next_node.left:
                queue.append(next_node.left)
                total += next_node.left.value
            if next_node.right:
                queue.append(next_node.right)
                total += next_node.right.value
            if total > 0:
                sum_of_levels.append(total)
                total -= total
        return sum_of_levels

    def get_height(self, start: Optional[TreeNode]) -> int:
        if start is None:
            return -1

        left_height = self.get_height(start.left)
        right_height = self.get_height(start.right)

        return 1 + max(left_height, right_height)

def pre_order_dfs(node: Optional[TreeNode]) -> None:
    if not node:
        return
    print(node.value)

    pre_order_dfs(node.left)
    pre_order_dfs(node.right)
