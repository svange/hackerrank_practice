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


class TestSolution(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve([1, 2, 3]), 0)
        self.assertEqual(solve([3, 2, 1]), 0)
        self.assertEqual(solve([1, 1, 1, 2, 2]), 8)
        self.assertEqual(solve([3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3]), 14)


if __name__ == '__main__':
    unittest.main()
