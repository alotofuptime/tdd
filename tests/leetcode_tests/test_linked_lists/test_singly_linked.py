from typing import Iterable
from tdd.leetcode.linked_lists.singly_linked import LinkedList
import pytest

class TestSinglyLinkedList:

    def test_empty_linked_list(self):
        llist = LinkedList()
        assert (llist.is_empty() is True) and (not llist.head and llist.tail is llist.head)

    @pytest.mark.parametrize("nodes",
                             [
                                 [9, 2, 11, 4],
                                 {"first":1, 2:2, 3:3},
                                 ("this", "is", "a", "tuple")
                             ]
    )
    def test_append_all(self, nodes):
        llist = LinkedList()
        if isinstance(nodes, dict):
            with pytest.raises(TypeError) as err:
                assert llist.append_all(nodes) is err
        else:
            llist.append_all(nodes)
            assert str(llist) == " -> ".join([str(node) for node in nodes])
            assert llist.size == len(nodes)

    @pytest.mark.insertion()
    def test_append(self):
        llist = LinkedList()
        llist.append(6)
        llist.append(7)
        llist.append(8)
        llist.append(9)
        assert (llist.size == 4) and (llist.tail.data == 9 and llist.head.data == 6)
        assert str(llist) == "6 -> 7 -> 8 -> 9"

    def test_new_node_cls_method(self):
        llist = LinkedList()
        llist.head = llist.new_node(9)
        llist.head = llist.new_node(llist.ListNode(8))
        assert isinstance(llist.head, llist.ListNode)
        assert (llist.tail.data) == 9 and (isinstance(llist.tail, llist.ListNode))
        assert llist.size == 2

    @pytest.mark.parametrize("nodes, data, idx",
                             [
                                 ([1, 2, 3, 4, 5], 4, 6),
                                 ([1, 2, 3, 4, 5], 6, "4")
                              ]

    )
    def test_insert_nth_invalid_idx(self, nodes, data, idx):
        llist = LinkedList()
        llist.append_all(nodes)
        if not isinstance(idx, int):
            with pytest.raises(TypeError) as err:
                assert llist.insert_nth(data, idx) is err
        if isinstance(idx, int) and (idx > llist.size):
            with pytest.raises(IndexError) as err:
                assert llist.insert_nth(data, idx) is err

    #TODO test insert_nth for valid index
    @pytest.mark.parametrize("nodes, data, idx",
                             [
                                 ([1, 2, 3, 4, 5], 4.5, 4),
                             ])
    def test_insert_nth_idx_is_length(self, nodes, data, idx):
        llist = LinkedList()
        llist.append_all(nodes)
        llist.insert_nth(data, idx)
        assert llist[4].data == 4.5
        assert llist.tail.data == 5
        assert len(llist) == (len(nodes) + 1)

    def test_update_node_data(self):
        llist = LinkedList(9)
        llist.head.data = 11
        assert llist.head.data == 11
        llist[0] = 12
        assert llist.head.data == 12

    @pytest.mark.deletion()
    def test_delete_head(self):
        llist = LinkedList(9)
        llist.append(10)
        llist.append(7)
        llist.append(5)
        llist.delete_head()
        assert llist.head.data == 10
        assert llist.size == 3
        assert str(llist) == "10 -> 7 -> 5"

    @pytest.mark.deletion()
    def test_delete_tail(self):
        llist = LinkedList(9)
        llist.append(10)
        llist.append(5)
        llist.append(8)
        llist.append(4)
        llist.delete_tail()
        assert (llist.tail.data == 8) and (llist.size == 4)
        assert str(llist) == "9 -> 10 -> 5 -> 8"

    @pytest.mark.deletion()
    @pytest.mark.parametrize("nodes, idx",
                             [
                                 ([100, 300, 24, 270, 45], "0"),
                                 ([100, 300, 24, 270, 45], 5),
                             ]
    )
    def test_delete_nth_invalid_idx(self, nodes, idx):
        llist = LinkedList()
        llist.append_all(nodes)
        if not isinstance(idx, int):
            with pytest.raises(TypeError) as err:
                assert llist.delete_nth(idx) is err
        if isinstance(idx, int) and (idx > len(llist)):
            with pytest.raises(IndexError) as err:
               assert llist.delete_nth(idx) is err

    def test_get_nth(self):
        llist = LinkedList(2)
        llist.prepend(6)
        llist.prepend(7)
        llist.append(8)
        llist.append(3)
        llist.append(4)
        assert llist.size == 6
        assert str(llist) == "7 -> 6 -> 2 -> 8 -> 3 -> 4"
        fourth_node = llist.get_nth(3)
        assert (fourth_node.data == 8) and (llist[3] == fourth_node)
        with pytest.raises(IndexError):
            llist.get_nth(7)

    @pytest.mark.parametrize("nodes, target",
                             [
                                 ([1, 2, 3, 4, 5], 0),
                                 ([6, 3, 21, 39, 4, 40], 21),
                                 ([7, 17, 28, 34, 100, 307], 100),
                                 ([5, 10, 9, 47, 8], 11)
                             ]
    )
    def test_search(self, nodes, target):
        llist = LinkedList()
        llist.append_all(nodes)
        assert llist.size == len(nodes)
        assert str(llist) == " -> ".join([str(node) for node in nodes])
        assert llist.search(target) == (target in nodes)

    @pytest.mark.parametrize("sequence",
                             [
                                 [8, 9, 10],
                                 [7, 189, 7, 39, 20],
                                 ["j", "aj", "yah"],
                                 []
                             ]
    )
    def test_reverse(self, sequence):
        llist = LinkedList()
        llist.append_all(sequence)
        llist.reverse()
        reverse_seq = reversed(sequence)
        expected_result = " -> ".join([str(item) for item in reverse_seq])
        assert llist.size == len(sequence)
        assert str(llist) == expected_result


    @pytest.mark.parametrize("nodes, idx, data",
                             [
                                 ([1, 2, 3, 4, 5], 0, 4),
                                 ([6, 7, 8, 9, 10], 1, 3),
                                 (["j", "o", "s", "h"], "0", "J")
                             ]
    )
    def test_update(self, nodes, idx, data):
        llist = LinkedList()
        llist.append_all(nodes)
        if not isinstance(idx, int):
            with pytest.raises(TypeError) as err:
                assert llist.update(idx, data) is err
        else:
            llist.update(idx,data)
            assert llist[idx].data == data

