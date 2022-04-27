from typing import Optional
from tdd.leetcode.linked_lists.singly_linked import LinkedList

def reverse_sublist(head: LinkedList.ListNode, start: int, end: int) -> Optional[LinkedList.ListNode]:
    prev = dummy = LinkedList.ListNode(-1)
    dummy.next = curr = head
    curr_pos = 1

    while curr and curr_pos != start:
        prev, curr = (curr, curr.next)
        curr_pos += 1
    sublist_head = curr

    while sublist_head and curr_pos != end:
        temp = sublist_head.next
        sublist_head.next = temp.next
        temp.next = prev.next
        prev.next = temp
        curr_pos += 1
    return dummy.next

