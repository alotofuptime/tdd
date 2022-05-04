import pytest
from tdd.leetcode.stacks_and_queues.linked_stack import LinkedStack

class TestLinkedStack:
    @pytest.fixture()
    def empty_stack(self):
        empty_stack = LinkedStack()
        return empty_stack

    def test_empty_stack(self, empty_stack):
        assert empty_stack.top is None
        assert empty_stack.bottom is None
        assert empty_stack.size == 0

    @pytest.mark.parametrize("data",
        [
            [7],
            [8],
            [9],
            [10],
            [11]
        ]
    )
    def test_new_node(self, data, empty_stack):
        new_node = empty_stack.new_node(data)
        assert isinstance(new_node, LinkedStack.StackNode)
        assert new_node.data == data and new_node.nxt is None

