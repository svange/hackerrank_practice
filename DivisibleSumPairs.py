import unittest
import itertools
import functools


def divisible_sum_pairs(n, k, arr):
    return functools.reduce(lambda x, y: x + y, (1 for x, y in itertools.permutations(arr, 2) if (x + y) % k == 0)) / 2


class TestDivisibleSumPairs(unittest.TestCase):
    def test_divisible_sum_pairs(self):
        self.assertEqual(divisible_sum_pairs(6, 3, [1, 3, 2, 6, 1, 2]), 5)


if __name__ == '__main__':
    unittest.main()
