from tdd.leetcode.linked_lists.singly_linked import LinkedList

class TestSinglyLinkedList:

    def test_empty_linked_list(self):
        llist = LinkedList()
        assert (llist.is_empty() is True) and (not llist.head and llist.tail is llist.head)

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

    def test_prepend(self):
        llist = LinkedList()
        llist.prepend(90)
        llist.prepend(LinkedList.ListNode(100))
        assert (llist.head.data == 100) and (llist.tail.data == 90)
        assert llist.size == 2

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

    #TODO test llist[n] = x (mabye this should be for insert and not update?)
    def test_update_node_data(self):
        llist = LinkedList(9)
        llist.head.data = 11
        assert llist.head.data == 11

    def test_delete_head(self):
        llist = LinkedList(9)
        llist.append(10)
        llist.append(7)
        llist.append(5)
        llist.delete_head()
        assert llist.head.data == 10
        assert llist.size == 3
        assert str(llist) == "10 -> 7 -> 5"

    def test_delete_tail(self):
        llist = LinkedList(9)
        llist.append(10)
        llist.append(5)
        llist.append(8)
        llist.append(4)
        llist.delete_tail()
        assert (llist.tail.data == 8) and (llist.size == 4)
        assert str(llist) == "9 -> 10 -> 5 -> 8"

    def test_delete_nth(self):
        llist = LinkedList(2)
        llist.append(3)
        llist.append(5)
        llist.append(8)
        llist.prepend(4)
        llist.delete_nth(2)
        assert llist.size == 4
        assert str(llist) == "4 -> 2 -> 5 -> 8"

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

    def test_search(self):
        llist = LinkedList(4)
        llist.append(3)
        llist.append(0)
        llist.append(5)
        llist.append(9)
        llist.prepend(10)
        assert llist.size == 6
        assert str(llist) == "10 -> 4 -> 3 -> 0 -> 5 -> 9"
        assert (llist.search(3) is True) and (llist.search(11) is False)
        assert (3 in llist) and (11 not in llist)

    def test_reverse(self):
        llist = LinkedList(9)
        llist.append(10)
        llist.append(11)
        llist.append(12)
        llist.append(13)
        llist.reverse()
        assert str(llist) == "13 -> 12 -> 11 -> 10 -> 9"
        assert llist.size == 5

    def test_update(self):
        llist = LinkedList(9)
        llist.append(6)
        llist.append(2)
        llist.append(5)
        llist.append(7)
        llist.update(3, 10)
        assert str(llist) == "9 -> 6 -> 2 -> 10 -> 7"


