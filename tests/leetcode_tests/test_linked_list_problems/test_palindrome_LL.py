from tdd.leetcode.linked_lists.singly_linked import LinkedList
from tdd.leetcode.linked_list_problems.palindrome_LL import get_middle_node, reverse_second_half, is_palindrome_llist
import pytest

class TestPalindromeLL:

    @pytest.mark.parametrize("nodes",
                             [
                                 [1, 2, 2, 1],
                                 [2, 4, 6, 4, 2]
                             ]
    )
    def test_get_middle_node(self, nodes):
        llist = LinkedList()
        llist.append_all(nodes)
        mid = len(nodes) // 2
        result = get_middle_node(llist.head)
        assert result.data == nodes[mid]


    @pytest.mark.parametrize("nodes",
                             [
                                 [1, 2, 2, 1],
                                 [2, 4, 6, 4, 2]
                             ]
    )
    def test_reverse_second_half(self, nodes):
        llist = LinkedList()
        llist.append_all(nodes)
        mid_node = get_middle_node(llist.head)
        reverse_second_half(mid_node)
        assert llist.tail.next.data == nodes[-2]


    @pytest.mark.parametrize("nodes",
                             [
                                 [1, 2, 2, 1],
                                 [2, 4, 6, 4, 2]
                             ]
    )
    def test_is_palindrome_llist(self, nodes):
        llist = LinkedList()
        llist.append_all(nodes)
        assert is_palindrome_llist(llist.head) is True
        assert str(llist) == " -> ".join([str(node) for node in nodes])

