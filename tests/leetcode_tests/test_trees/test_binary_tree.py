import pytest
from tdd.leetcode.trees.binary_tree import BinaryTree, TreeNode, pre_order_dfs

class TestBinaryTree(object):
    @pytest.fixture()
    def empty_tree(self):
        return BinaryTree()

    @pytest.fixture()
    def empty_tree_node(self):
        return TreeNode()

    @pytest.fixture()
    def tree(self):
        tree = BinaryTree()
        tree.root = TreeNode(1)
        tree.root.left = TreeNode(2)
        tree.root.right = TreeNode(3)
        return tree

    def test_empty_tree(self, empty_tree):
        assert empty_tree.root is None

    def test_empty_tree_node(self, empty_tree_node):
        assert empty_tree_node.value is None

    def test_populated_tree(self, tree):
        assert isinstance(tree.root, TreeNode)
        assert isinstance(tree.root.left, TreeNode)
        assert isinstance(tree.root.right, TreeNode)
        assert tree.root.value == 1
        assert tree.root.left.value == 2
        assert tree.root.right.value == 3

    def test_pre_order_dfs(self, tree, capsys):
        pre_order_dfs(tree.root)
        captured = capsys.readouterr()
        assert captured.out == "1\n2\n3\n"

    def test_pre_order_traversal(self, tree):
        result = tree.pre_order(tree.root)
        assert result == "1 - 2 - 3 - "

    def test_in_order_traversal(self, tree):
        result = tree.in_order(tree.root)
        assert result == "2 - 1 - 3 - "

    def test_post_order_traversal(self, tree):
        result = tree.post_order(tree.root)
        assert result == "2 - 3 - 1 - "

    def test_level_order_traversal(self, tree):
        tree.root.left.left = TreeNode(4)
        tree.root.right.right = TreeNode(5)
        result = tree.level_order(tree.root)
        assert result == "1 - 2 - 3 - 4 - 5 - "

