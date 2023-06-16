import pytest
from ll import Node


def test_node_1():
    actual = Node(1)
    expected = 1
    assert actual.value == expected


def test_node_next():
    node1 = Node(1)
    node2 = Node(2, node1)
    actual = node2._next
    expected = node1
    assert actual == expected
