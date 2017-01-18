import unittest

# AI classes
from environment import Environment


class GeneralTests(unittest.TestCase):

    def __init__(self): pass

    def test_envioronment_init(self):
        env = Environment(10, 10)
        assert env not None