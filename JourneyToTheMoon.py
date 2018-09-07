import unittest, collections
from typing import List


def journey_to_the_moon(astronaut_pairs: List[List[int]]):
    # Create an adj list
    for x, y in astronaut_pairs:





    adj_list = []
    connected_components = {}
    component = 0
    for node, neighbors in enumerate(adj_list):
        q = collections.deque()
        visited = set()
        q.append(node)
        while q:
            current = q.popleft()
            if current in visited:
                continue
            visited.add(current)
            connected_components[current] = component
            q.extend(adj_list[current])
        component += 1

    print(str(connected_components))





class TestJourneyToTheMoon(unittest.TestCase):
    def test_solution_1(self):
        self.assertEqual(journey_to_the_moon([[0, 1], [3, 2], [3, 4]]), 6)


if __name__ == '__main__':
    unittest.main()