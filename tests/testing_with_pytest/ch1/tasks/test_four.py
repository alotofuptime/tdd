# Test the Task data type
from collections import namedtuple
import time
import pytest

Task = namedtuple("Task", ["summary", "owner", "done", "id"])
Task.__new__.__defaults__ = (None, None, False, None)

#@pytest.mark.run_these_please
def test_asdict():
    # _asdict() should return a dictionary
    t_task = Task("do something", "okken", True, 21)
    t_dict = t_task._asdict()
    expected = {
        "summary": "do something",
        "owner": "okken",
        "done": True,
        "id": 21
    }
    assert t_dict == expected

#@pytest.mark.run_these_please
def test_replace():
    t_before = Task("finish book", "brian", False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task("finish book", "brian", True, 11)
    time.sleep(0.1)
    assert t_after == t_expected
