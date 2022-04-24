from tdd.leetcode.linked_lists.singly_linked import LinkedList
from typing import Optional

def get_middle_node(head: LinkedList.ListNode) -> LinkedList.ListNode:
    slow = fast = head
    while (fast and fast.next):
        slow, fast = (slow.next, fast.next.next)
    return slow

def reverse_second_half(mid_node: LinkedList.ListNode) -> LinkedList.ListNode:
    prev = curr = mid_node
    nxt = curr.next
    curr.next = None
    curr = nxt

    while curr:
        nxt = curr.next
        curr.next = prev
        prev, curr = (curr, nxt)
    return prev

def is_palindrome_llist(head: LinkedList.ListNode) -> bool:
    dummy_ptr = dummy = LinkedList.ListNode(-1)
    dummy_ptr.next = head
    dummy_ptr = dummy_ptr.next
    mid_node = get_middle_node(dummy_ptr)
    tail_node = reverse_second_half(mid_node)

    curr1, curr2 = (dummy_ptr, tail_node)
    while curr1 is not curr2:
        if curr1.data != curr2.data:
            return False
        if curr1.next is curr2:
            break
        curr1, curr2 = (curr1.next, curr2.next)
    return True
