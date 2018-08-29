import unittest


class Mark:
    def __init__(self, cupcakes):
        self.cupcakes = cupcakes

    def min_walk(self):
        self.cupcakes.sort()
        self.cupcakes.reverse()
        poly = list(zip(self.cupcakes, range(len(self.cupcakes))))
        # print ('poly: ' + str(list(poly)))
        solved = [p[0] * (2 ** p[1]) for p in poly]
        # print ('solved: ' + str(list(solved)))
        return sum(solved)


class TestMark(unittest.TestCase):
    def test_min_walk(self):
        self.assertEqual(Mark([1, 2, 3]).min_walk(), 11)
        self.assertEqual(Mark([3, 2, 1]).min_walk(), 11)
        self.assertEqual(Mark([1, 3, 2]).min_walk(), 11)
        self.assertNotEqual(Mark([1, 3, 2]).min_walk(), 12)


if __name__ == "__main__":
    unittest.main()
