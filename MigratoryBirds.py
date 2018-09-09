import unittest
from collections import defaultdict
import functools


def migratory_birds(arr):
    sighting_table = defaultdict(lambda: 0)
    for bird in arr:
        sighting_table[bird] += 1
    max_count = functools.reduce(lambda x, y: x if x[1] > y[1] else y , sighting_table.items())[1]
    most_seen = (bird for bird, sightings in sighting_table.items() if sightings == max_count)
    return min(most_seen)


class TestMigratoryBirds(unittest.TestCase):
    def test_migratory_birds(self):
        self.assertEqual(migratory_birds([1, 2, 2, 3, 3, 4, 2, 3] * 1000000), 2) # list of length 8,000,000


if __name__ == '__main__':
    unittest.main()
