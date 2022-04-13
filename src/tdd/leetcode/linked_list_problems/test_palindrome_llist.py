from tdd.leetcode.linked_lists.singly_linked import LinkedList

def cache_and_reverse(head: LinkedList.ListNode) -> tuple:
    dummy = LinkedList.ListNode(-1)
    dummy_ptr = dummy
    curr, prev = head, None
    dummy_ptr.next = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev, dummy.next


def is_palindrome(head1: LinkedList.ListNode, head2: LinkedList.ListNode) -> bool:
    curr1, curr2 = head1, head2
    while curr1 and curr2:
        if curr1.val != curr2.val:
            return False
        curr1, curr2 = curr1.next, curr2.next
    return True


def print_list(head: LinkedList.ListNode) -> str:
    result = head
    nodes = []
    while result:
        nodes.append(result.val)
        result = result.next

    return " -> ".join([str(item) for item in nodes])



class TestPalindromeLinkedList:

    def test_cache_and_reverse_helper_func(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(2)
        llist.append(1)
        result = cache_and_reverse(llist.head)
        assert type(result) is tuple

    def test_is_palindrome_main_func(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(2)
        llist.append(1)
        result = cache_and_reverse(llist.head)
        assert is_palindrome(result[0], result[1]) is True
