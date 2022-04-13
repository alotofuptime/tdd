from tdd.leetcode.linked_lists.singly_linked import LinkedList
from tdd.leetcode.linked_list_problems.palindrome_LL import cache_and_reverse, is_palindrome, print_list

class TestPalindromeLL:

    def test_cache_and_reverse(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(2)
        llist.append(1)
        head1, head2 = cache_and_reverse(llist.head)
        assert (head1 != llist.tail) and (head2 == llist.head)


