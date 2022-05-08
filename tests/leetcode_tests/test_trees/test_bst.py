import random

import pytest
from tdd.leetcode.trees.bst import BinarySearchTree

class TestBST(object):
    @pytest.fixture()
    def bst(self):
        bst = BinarySearchTree()
        nodes = [i for i in range(1000)]
        random.shuffle(nodes)
        for node in nodes:
            bst.insert(node)
        return bst

    @pytest.fixture()
    def empyt_bst(self):
        return BinarySearchTree()

    @pytest.fixture()
    def nodes(self):
        nodes = [i for i in range(1000)]
        random.shuffle(nodes)
        return nodes

    def test_bst_insert(self, bst):
        assert bst.root is not None
        assert bst.root.leftChild.parent is bst.root

    @pytest.mark.parametrize(
        "values",
        [
            [i for i in range(100)]
        ]
    )
    def test_bst_insert_duplicate(self, bst, values):
        random.shuffle(values)
        for val in values:
            assert bst.insert(val) == False

    def test_bst_insert_recursive(self, empyt_bst, nodes):
        tree = empyt_bst
        for node in nodes:
            tree.insert_recursive(node)

        left_child, right_child = (
            tree.root.leftChild.data,
            tree.root.rightChild.data
        )
        assert left_child < tree.root.data < right_child

    @pytest.mark.parametrize(
        "values",
        [
            [i for i in range(100)]
        ]
    )
    def test_bst_insert_recursive_duplicate(self, bst, values, capsys):
        random.shuffle(values)
        for val in values:
            bst.insert_recursive(val)
            captured = capsys.readouterr()
            assert captured.out.strip() == f"ENTRY FAILED: {str(val)} already exists. Entries must be unique."

    @pytest.mark.parametrize(
        "target",
        [
            [8],
            [4],
            [3],
            [6],
            [9],
            [9090],
            [8923],
            [29798],
        ]
    )
    def test_bst_search(self, bst, target, nodes):
        target = target[0]
        if target in nodes:
            result = bst.search(target)
            assert result.data == target
        else:
            assert bst.search(target) == False

    @pytest.mark.parametrize(
        "target",
        [
            [8],
            [4],
            [3],
            [6],
            [9],
            [9090],
            [8923],
            [29798],
        ]
    )
    def test_bst_search_recursive(self, bst, target, nodes):
        target = target[0]
        if target in nodes:
            result = bst.search_recursive(target)
            assert result.data == target
        else:
            assert bst.search_recursive(target) == False

    @pytest.mark.parametrize(
        "target",
        [
            [8],
            [4],
            [3],
            [6],
            [9],
        ]
    )
    def test_bst_delete(self, bst, target, nodes):
        target = target[0]
        bst.delete(target)
        assert bst.search(target) is False

