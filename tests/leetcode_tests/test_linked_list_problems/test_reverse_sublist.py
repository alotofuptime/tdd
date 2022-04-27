import pytest
from tdd.leetcode.linked_lists.singly_linked import LinkedList
from tdd.leetcode.linked_list_problems.reverse_sub_list import reverse_sublist

class TestReverseSublist:
    @pytest.fixture()
    def input_list(self):
        nodes = [1, 2, 3, 4, 5]
        llist = LinkedList()
        llist.append_all(nodes)
        return llist

    def test_reverse_sublist(self, input_list):
        result = reverse_sublist(input_list.head, 2, 4)
        output_list = LinkedList(result)
        expected_output = "1 -> 4 -> 3 -> 2 -> 5"
        assert str(output_list) == expected_output
