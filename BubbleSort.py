import unittest
import math

class Sortable:
    def __init__(self, items):
        self.items = list(items)
        self.swaps = 0
        self.bubble_sort()
        self.min = self.items[0]
        self.max = self.items[-1]

    def bubble_sort(self):
        for i in range(len(self.items)):
            local_swaps = 0
            for j in range(len(self.items) - 1):
                if self.items[j] > self.items[j + 1]:
                    tmp = self.items[j]
                    self.items[j] = self.items[j + 1]
                    self.items[j + 1] = tmp
                    local_swaps += 1
            self.swaps += local_swaps
            if local_swaps == 0:
                break


class TestSortable(unittest.TestCase):
    def test_bubble_sort(self):
        test_list = [3, 2, 1]
        s = Sortable(test_list)
        s_min = s.min
        s_max = s.max
        s_swaps = s.swaps
        self.assertEqual(1, s_min)
        self.assertEqual(3, s_max)
        self.assertEqual(3, s_swaps)


if __name__ == "__main__":
    unittest.main()
