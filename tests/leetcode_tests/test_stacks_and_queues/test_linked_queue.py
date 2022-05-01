import pytest
from tdd.leetcode.stacks_and_queues.linked_queue import LinkedQueue

class TestLinkedQueue:
    @pytest.fixture
    def (self):
        queue = LinkedQueue()
        return queue

    @pytest.fixture
    def queue_with_front(self):
        queue = LinkedQueue(9)
        return queue

    def test_empty_queue(self, empty_queue):
        assert empty_queue.is_empty() is True

    def test_queue_with_front(self, queue_with_front):
        assert isinstance(queue_with_front.front, LinkedQueue.QueueNode)
        assert queue_with_front.front is queue_with_front.rear
        assert queue_with_front.size == 1

    @pytest.mark.parametrize("node", [7])
    def test_enqueue_empty_queue(self, empty_queue, node):
        empty_queue.enqueue(node)
        assert isinstance(empty_queue.front, LinkedQueue.QueueNode)
        assert empty_queue.front.data == 7
        assert empty_queue.rear.data == 7
        assert empty_queue.size == 1

    @pytest.mark.parametrize("node", [7])
    def test_enqueue_queue_with_front(self, queue_with_front, node):
        original_front = queue_with_front.front.data
        queue_with_front.enqueue(node)
        assert isinstance(queue_with_front.front, LinkedQueue.QueueNode)
        assert queue_with_front.front.data == original_front
        assert queue_with_front.front.nxt is queue_with_front.rear
        assert queue_with_front.rear.data == 7
        assert queue_with_front.size == 2

    @pytest.mark.parametrize("nodes",
                             [
                                 [1, 2, 3, 4, 5],
                                 ["nodes", "of", "strings", "to", "test"],
                                 [(1, 2), (3, 4), (5, 6)],
                                 {1: "one", 2: "two", 3: "three"}
                             ]
    )
    def test_enqueue_all_empty_queue(self, empty_queue, nodes):
        empty_queue.enqueue_all(nodes)
        assert test_queue.front.data == nodes[0]
        assert test_queue.size == len(nodes)

    @pytest.mark.parametrize("node",
                             [
                                 [7],
                                 [8],
                                 [9],
                                 [6],
                                 [5],
                             ]
    )
    def test_new_node_cls_method(self, node):
        result = LinkedQueue.new_node(node)
        assert isinstance(result, LinkedQueue.QueueNode)
        assert result.data == node

