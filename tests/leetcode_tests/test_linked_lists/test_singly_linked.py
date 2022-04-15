from typing import Iterable
from tdd.leetcode.linked_lists.singly_linked import LinkedList
import pytest

class TestSinglyLinkedList:

    def test_empty_linked_list(self):
        llist = LinkedList()
        assert (llist.is_empty() is True) and (not llist.head and llist.tail is llist.head)

    def test_append_all(self):
        llist = LinkedList()
        arr = [9, 2, 11, 20]
        llist.append_all(arr)
        assert str(llist) == "9 -> 2 -> 11 -> 20"
        assert llist.size == 4

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
    def test_prepend(self):
        llist = LinkedList()
        llist.prepend(90)
        llist.prepend(LinkedList.ListNode(100))
        assert (llist.head.data == 100) and (llist.tail.data == 90)
        assert llist.size == 2

    @pytest.mark.insertion()
    def test_insert_nth(self):
        llist = LinkedList()
        llist.prepend(9)
        llist.append(10)
        llist.append(11)
        llist.append(17)
        llist.insert_nth(8, 2)
        assert str(llist) == "9 -> 10 -> 8 -> 11 -> 17"
        assert (llist.head.data == 9 and llist.tail.data == 17)
        assert llist.size == 5
        assert llist.insert_nth(4, 6) is False
        with pytest.raises(TypeError) as excinfo:
            llist.insert_nth(7, "2")
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "idx must be of type int"

    #TODO test llist[n] = x
    def test_update_node_data(self):
        llist = LinkedList(9)
        llist.head.data = 11
        assert llist.head.data == 11

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
    def test_delete_nth(self):
        llist = LinkedList(2)
        llist.append(3)
        llist.append(5)
        llist.append(8)
        llist.prepend(4)
        llist.delete_nth(2)
        assert llist.size == 4
        assert str(llist) == "4 -> 2 -> 5 -> 8"
        with pytest.raises(IndexError) as excinfo:
            llist.delete_nth(7)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Index out of range"

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
                             [([1, 2, 3, 4, 5], 0),
                              ([6, 3, 21, 39, 4, 40], 21),
                              ([7, 17, 28, 34, 100, 307], 100),
                              ([5, 10, 9, 47, 8], 11)])
    def test_search(self, nodes, target):
        llist = LinkedList()
        llist.append_all(nodes)
        assert llist.size == len(nodes)
        assert str(llist) == " -> ".join([str(node) for node in nodes])
        assert llist.search(target) == (target in nodes)

    @pytest.mark.parametrize("sequence",
                             [[8, 9, 10],
                              [7, 189, 7, 39, 20],
                              ["j", "aj", "yah"],
                              []])
    def test_reverse(self, sequence):
        llist = LinkedList()
        llist.append_all(sequence)
        llist.reverse()
        reverse_seq = reversed(sequence)
        expected_result = " -> ".join([str(item) for item in reverse_seq])
        assert llist.size == len(sequence)
        assert str(llist) == expected_result


    def test_update(self):
        llist = LinkedList(9)
        llist.append(6)
        llist.append(2)
        llist.append(5)
        llist.append(7)
        llist.update(3, 10)
        llist[1] = 5
        assert str(llist) == "9 -> 5 -> 2 -> 10 -> 7"
