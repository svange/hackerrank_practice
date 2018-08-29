import unittest


class NothingClass:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x


class TestStringMethods(unittest.TestCase):

    def test_basic(self):
        self.assertTrue(1, NothingClass(1).x)


if __name__ == '__main__':
    unittest.main()