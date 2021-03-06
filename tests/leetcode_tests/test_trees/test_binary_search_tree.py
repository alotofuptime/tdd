import random
import pytest
from tdd.leetcode.trees.binary_search_tree import BinarySearchTree

class TestBinarySearchTree:
    @pytest.fixture()
    def empty_bst(self):
        tree = BinarySearchTree()
        return tree

    @pytest.fixture()
    def bst(self):
        tree = BinarySearchTree()
        nodes = [9, 27, 1, 38, 17, 5]
        random.shuffle(nodes)
        for node in nodes:
            tree.insert(node)
        return tree

    def test_empty_bst(self, empty_bst):
        assert empty_bst.root is None

    def test_bst_insert(self, bst):
        node = bst.root
        assert node.data is not None
        assert (node.left.parent is node) and (node.right.parent is node)
        assert bst.is_bst() is True

    @pytest.mark.parametrize("nodes",
        [
            [1, 2, 3, 4, 5],
            [2, 4, 6, 8, 10],
            ["Josh", "Kianna", "Demitri", "Ruthie", "Carlos", "Joe", "Kate", "Cook"],
        ]
    )
    def test_bst_insert_parametrized(self, empty_bst, nodes):
        tree = empty_bst
        random.shuffle(nodes)
        for node in nodes:
            tree.insert(node)

        assert tree.search(nodes[0]) is nodes[0]
        assert tree.search("absent val") is False
        assert tree.is_bst() is True

    def test_is_bst(self, bst):
        assert bst.is_bst() is True

    def test_dfs_inorder(self, bst):
        assert bst.dfs_inorder(bst.root) == [1, 5, 9, 17, 27, 38]

    def test_bst_search(self, bst):
        assert bst.search(40) == False
        assert bst.search(17) == 17

    @pytest.mark.parametrize("nodes",
        [
            [1, 2, 3, 4, 5],
            [2, 4, 6, 8, 10],
            ["Josh", "Kianna", "Demitri", "Ruthie", "Carlos", "Joe", "Kate", "Cook"],
        ]
    )
    def test_bst_update_parametrized(self, empty_bst, nodes):
        tree = empty_bst
        random.shuffle(nodes)
        for node in nodes:
            tree.insert(node)

        assert tree.search(nodes[0]) is nodes[0]

        if isinstance(nodes[0], str):
            assert tree.update(nodes[0], "JOSH")
            assert tree.search("JOSH") is "JOSH"
        else:
            assert tree.update(nodes[0], 17)
            assert tree.search(17) == 17

        assert tree.search("absent val") is False
        assert tree.is_bst() is True

    @pytest.mark.parametrize("nodes",
        [
            [1, 2, 3, 4, 5],
            [2, 4, 6, 8, 10],
            ["Josh", "Kianna", "Demitri", "Ruthie", "Carlos", "Joe", "Kate", "Cook"],
        ]
    )
    def test_bst_delete_parametrized(self, empty_bst, nodes):
        tree = empty_bst
        random.shuffle(nodes)
        for node in nodes:
            tree.insert(node)

        tree.delete(nodes[0])
        assert tree.search(nodes[0]) is False
        assert tree.is_bst() is True


