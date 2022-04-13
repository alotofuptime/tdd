from tdd.leetcode.linked_lists.singly_linked import LinkedList

class TestSinglyLinkedList:

    def test_empty_linked_list(self):
        llist = LinkedList()
        assert (llist.is_empty() is True) and (not llist.head and llist.tail is llist.head)

    def test_append_single_value_to_empty_list(self):
        llist = LinkedList()
        llist.append(0)
        assert (llist.head.data == 0) and (llist.head.next is None)
        assert isinstance(llist.head, LinkedList.ListNode)
        assert (llist.tail is llist.head) and (llist.size == 1)
        assert llist.is_empty() is False

    def test_append_single_value_to_non_empty_list(self):
        llist = LinkedList(0)
        llist.append(1)
        assert (llist.head.data == 0) and (llist.tail.data == 1)
        assert llist.size == 2

    def test_append_multiple_values_to_empty_or_non_empty_list(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        result = " -> ".join([str(node.data) for node in llist])
        assert (llist.tail.data == 3)
        assert (llist.size == len([node for node in llist]))
        assert (llist.head.next.data == 2)
        assert result == str(llist)

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
