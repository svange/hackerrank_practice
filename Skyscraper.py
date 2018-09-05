import functools
import unittest


def solve(arr):
    if len(arr) <= 1:
        return 0

    tallest = max(arr)
    num_tallest = arr.count(tallest)

    tallest_paths = num_tallest * (num_tallest - 1)

    splits = [i for i, x in enumerate(arr) if x == tallest]

    sub_problems = []
    current = 0
    for split in splits:
        sub_problems.append(arr[current:split])
        current = split + 1
    if current == len(arr) + 1:
        sub_problems.append(arr[current::])

    sub_problem_answers = map(solve, sub_problems)
    sum_sub_problem_answers = functools.reduce(lambda x, y: x + y, sub_problem_answers)

    return int(tallest_paths + sum_sub_problem_answers)

def solve_stack(arr):
    if len(arr) <= 1:
        return 0
    stack = []

    num_paths = 0
    first_seen = {}

    for next_building in arr:
        if len(stack) == 0:
            stack.append(next_building)
            first_seen[next_building] = len(stack) - 1
            continue

        if next_building > stack[-1]:

            #############################################################################

            while next_building > stack[-1]:
                stack = stack[:first_seen[stack[-1]]]
                for key in first_seen.keys():
                    if key < next_building:
                        first_seen[key] = None
                    if len(stack) == 0:
                        break

            #############################################################################

            # while next_building > stack[-1]:
            #     stack.pop()
            #     if len(stack) == 0:
            #         break

            #############################################################################

            if len(stack) > 0 and next_building == stack[-1]:
                num_paths += stack.count(next_building) * 2
            if not first_seen.get(next_building):
                first_seen[next_building] = len(stack) - 1
            stack.append(next_building)
        elif next_building < stack[-1]:
            if not first_seen.get(next_building):
                first_seen[next_building] = len(stack) - 1
            stack.append(next_building)
        elif next_building == stack[-1]:
            num_paths += stack.count(next_building) * 2
            if not first_seen.get(next_building):
                first_seen[next_building] = len(stack) - 1
            stack.append(next_building)
    return num_paths



class TestSolution(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve([1, 2, 3]), 0)
        self.assertEqual(solve([3, 2, 1]), 0)
        self.assertEqual(solve([1, 1, 1, 2, 2]), 8)
        self.assertEqual(solve([3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3]), 14)

    def test_solve_stack(self):
        self.assertEqual(solve_stack([1, 2, 3]), 0)
        self.assertEqual(solve_stack([3, 2, 1]), 0)
        self.assertEqual(solve_stack([1, 1, 1, 2, 2]), 8)
        self.assertEqual(solve_stack([3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3]), 14)


if __name__ == '__main__':
    unittest.main()
