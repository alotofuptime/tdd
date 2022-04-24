from typing import Iterable
from tdd.leetcode.linked_lists.singly_linked import LinkedList
import pytest

class TestSinglyLinkedList:

    def test_empty_linked_list(self):
        llist = LinkedList()
        assert (llist.is_empty() is True) and (not llist.head and llist.tail is llist.head)

    @pytest.mark.insertion()
    @pytest.mark.parametrize("nodes",
                             [
                                 None,
                                 100
                             ]
    )
    def test_append_all_invalid_input(self, nodes):
        llist = LinkedList()
        with pytest.raises(TypeError) as err:
            assert llist.append_all(nodes) is err

    @pytest.mark.insertion()
    @pytest.mark.parametrize("nodes",
                             [
                                 {"key": "val", "night": "day"},
                                 (1, 2, 3, 4, 5, 6),
                                 [7, "list", "array", [2, 4]],
                                 {1, 8, 29, 0.9}
                             ]
    )
    def test_append_all_valid_input(self, nodes):
        llist = LinkedList()
        llist.append_all(nodes)
        assert str(llist) == " -> ".join([str(node) for node in nodes])

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

    @pytest.mark.insertion()
    @pytest.mark.parametrize("nodes, data, idx",
                             [
                                 ([1, 2, 3, 4, 5], 4, 6),
                                 ([1, 2, 3, 4, 5], 6, "4")
                              ]

    )
    def test_insert_nth_invalid_idx(self, nodes, data, idx):
        llist = LinkedList()
        llist.append_all(nodes)
        with pytest.raises((TypeError, IndexError)) as err:
            assert llist.insert_nth(data, idx) is err

    @pytest.mark.insertion()
    @pytest.mark.parametrize("nodes, data, idx",
                             [
                                 (["this", "is", "a", "test"], "test", 1),
                                 (["this", "is", "a", "test"], "not", 2),
                                 (["this", "is", "a", "test"], "wait", 0),
                                 (["this", "is", "a", "test"], "TEST", -1),
                                 (["this", "is", "a", "test"], "man", 3),
                             ]

    )
    def test_insert_nth_valid_idx(self, nodes, data, idx):
        llist = LinkedList()
        llist.append_all(nodes)
        llist.insert_nth(data, idx)
        assert llist[idx].data is data
        assert llist.size == (len(nodes) + 1)

    @pytest.mark.insertion()
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
    @pytest.mark.parametrize("nodes",
                             [
                                 [2, 4, 5, 8, 10],
                                 [4, 5, 8, 10],
                                 [5, 8, 10],
                                 [8, 10],
                                 [10],
                             ]
    )
    def test_delete_head(self, nodes):
        llist = LinkedList()
        llist.append_all(nodes)
        llist.delete_head()
        assert len(llist) == (len(nodes) - 1)
        if (len(nodes) > 1):
            assert llist.head.data == nodes[1]
        else:
            assert llist.head is None

    @pytest.mark.deletion()
    @pytest.mark.parametrize("nodes",
                             [
                                 ["random", "nodes", "to", "test"],
                                 ["random", "nodes", "to"],
                                 ["random", "nodes"],
                                 ["random"]
                             ]
    )
    def test_delete_tail(self, nodes):
        llist = LinkedList()
        llist.append_all(nodes)
        llist.delete_tail()
        if (len(nodes) > 1):
            assert llist.tail.data == nodes[-2]
        else:
            assert llist.tail is None
        assert len(llist) == (len(nodes) - 1)

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
        with pytest.raises((TypeError, IndexError)) as err:
            assert llist.delete_nth(idx) is err

    @pytest.mark.deletion()
    @pytest.mark.parametrize("nodes, idx",
                             [
                                 (["copy", "paste", "delete", "undo"], 0),
                                 (["copy", "paste", "delete", "undo"], 1),
                                 (["copy", "paste", "delete", "undo"], 2),
                                 (["copy", "paste", "delete", "undo"], 3),
                             ]
    )
    def test_delete_nth_valid_idx(self, nodes, idx):
        llist = LinkedList()
        llist.append_all(nodes)
        llist.delete_nth(idx)
        assert nodes[idx] not in llist
        assert len(llist) == (len(nodes) - 1)

    @pytest.mark.parametrize("nodes, idx",
                             [
                                 ([(1, 2), (3, 4), (5, 6), (7, 8)], "0"),
                                 ([(1, 2), (3, 4), (5, 6), (7, 8)], "1"),
                                 ([(1, 2), (3, 4), (5, 6), (7, 8)], 5),
                                 ([(1, 2), (3, 4), (5, 6), (7, 8)], 7),
                             ]
    )
    def test_get_nth_invalid_idx(self, nodes, idx):
        llist = LinkedList()
        llist.append_all(nodes)
        with pytest.raises((TypeError, IndexError)) as err:
            assert llist.get_nth(idx) is err

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
                                 (["j", "o", "s", "h"], "0", "J"),
                                 (["j", "o", "s", "h"], None, "J"),
                             ]
    )
    #TODO break this into valid and invlaid input tests
    def test_update_invalid_idx(self, nodes, idx, data):
        llist = LinkedList()
        llist.append_all(nodes)
        with pytest.raises(TypeError) as err:
            assert llist.update(idx, data) is err

    @pytest.mark.parametrize("nodes, idx, data",
                             [
                                 (["j", "o", "s", "h"], 0, "J"),
                                 (["j", "o", "s", "h"], -1, "H"),
                                 (["j", "o", "s", "h"], 1, "O"),
                                 (["j", "o", "s", "h"], 2, "S"),
                                 (["j", "o", "s", "h"], 3, "H"),
                             ]
    )
    def test_update_valid_idx(self, nodes, idx, data):
        llist = LinkedList()
        llist.append_all(nodes)
        llist.update(idx, data)
        assert llist[idx].data == data
