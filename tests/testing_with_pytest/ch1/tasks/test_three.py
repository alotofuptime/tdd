# Test the Task data type
from collections import namedtuple

Task = namedtuple("Task", ["summary", "owner", "done", "id"])
Task.__new__.__defaults__ = (None, None, False, None)

def test_defaults():
    # Using no params should invoke defalults
    t1 = Task()
    t2 = (None, None, False, None)
    assert t1 == t2

def test_memember_access():
    t = Task("buy milk", "brian")
    assert t.summary == "buy milk"
    assert t.owner == "brian"
    assert (t.done, t.id) == (False, None)
