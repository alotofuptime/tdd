import pytest
from tdd.leetcode.stacks_and_queues.linked_queue import LinkedQueue

class TestLinkedQueue:
    @pytest.fixture
    def empty_queue(self):
        queue = LinkedQueue()
        return queue

    @pytest.fixture
    def queue_with_front(self):
        queue = LinkedQueue(9)
        return queue

    def test_empty_queue(self, empty_queue):
        assert empty_queue.is_empty() is True
        assert len(empty_queue) == 0
        assert empty_queue.size == len(empty_queue)

    def test_queue_with_front(self, queue_with_front):
        assert isinstance(queue_with_front.front, LinkedQueue.QueueNode)
        assert queue_with_front.front is queue_with_front.rear
        assert len(queue_with_front) == 1

    @pytest.mark.parametrize("node", [7])
    def test_enqueue_empty_queue(self, empty_queue, node):
        empty_queue.enqueue(node)
        assert isinstance(empty_queue.front, LinkedQueue.QueueNode)
        assert empty_queue.front.data == 7
        assert empty_queue.rear.data == 7
        assert len(empty_queue) == 1

    @pytest.mark.parametrize("node", [7])
    def test_enqueue_queue_with_front(self, queue_with_front, node):
        queue_with_front.enqueue(node)
        assert isinstance(queue_with_front.front, LinkedQueue.QueueNode)
        assert queue_with_front.front.nxt is queue_with_front.rear
        assert queue_with_front.rear.data == 7
        assert len(queue_with_front) == 2

    @pytest.mark.parametrize("nodes",
                             [
                                 [1, 2, 3, 4, 5],
                                 ["nodes", "of", "strings", "to", "test"],
                                 [(1, 2), (3, 4), (5, 6)],
                                 {1: "one", 2: "two", 3: "three"}
                             ]
    )
    def test_enqueue_all_empty_queue(self, empty_queue, nodes):
        expected_repr = " -> ".join([str(node) for node in nodes])
        empty_queue.enqueue_all(nodes)
        if isinstance(nodes, dict):
            nodes = [node for node in nodes]
        assert empty_queue.front.data == nodes[0]
        assert empty_queue.rear.data == nodes[-1]
        assert len(empty_queue) == len(nodes)
        assert str(empty_queue) == expected_repr + " -> None"

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

    @pytest.mark.parametrize("nodes",
                             [
                                 [1, 2, 3, 4, 5],
                                 ["nodes", "of", "strings", "to", "test"],
                                 [(1, 2), (3, 4), (5, 6)],
                                 {1: "one", 2: "two", 3: "three"}
                             ]
    )
    def test_dequeue(self, empty_queue, nodes):
        queue = empty_queue
        queue.enqueue_all(nodes)
        next_node = queue.dequeue()
        if isinstance(nodes, dict):
            nodes = [node for node in nodes]
        assert next_node.data == nodes[0]
        assert len(queue) == (len(nodes) - 1)

    def test_dequeue_empty_queue(self, empty_queue):
        queue = empty_queue
        next_node = queue.dequeue()
        assert next_node is None
        assert len(queue) == 0

    @pytest.mark.parametrize("nodes",
        [
            [1, 2, 3, 4, 5, 6, 7],
            ["test", "the", "peek", "method", "test"],
            [(1, 2), (3, 4), (5, 6), (7,8)],
            {1: "one", 4: "four", 6: "six", 9: "nine"}
        ]


    )
    def test_peek(self, empty_queue, nodes):
        queue = empty_queue
        queue.enqueue_all(nodes)
        assert queue.peek() is queue.front
        assert len(queue) is len(nodes)

