import sys
import unittest


def maximum_subarray_and_subsequence(arr):
    maximum_subsequence_value = maximum_subsequence(arr)

    maximum_subarray_value = maximum_subarray(arr)

    return [maximum_subarray_value, maximum_subsequence_value]


def maximum_subsequence(arr):
    max_of_arr = max(arr)
    if max_of_arr < 0:
        max_subsequence_value = max_of_arr
    else:
        max_subsequence_value = sum([x for x in arr if x >= 0])
    return max_subsequence_value


def maximum_subarray(arr):
    # Fill the memo table with solutions for each subarray
    memo = {}
    maximum_subarray_helper(arr, memo)
    # Find the subarray with the solution of max value
    maximum_subarray_value = max([sum(memo[x]) for x in memo.keys()])
    return maximum_subarray_value


def maximum_subarray_helper(arr, memo):
    # Alias for readability
    # lists are mutable -> lists are not hashable
    # tuples are mutable -> tuples are hashable
    hash_func = tuple

    # subarrays of len 0 or 1 are their own solutions
    # base case
    if len(arr) <= 1:
        # keys for memo are
        memo[hash_func(arr)] = arr
        return arr

    # subproblem is finding the maximum_subarray of arr[:-1]
    # subproblem_solution is the solution of subproblem with the last item of arr appended to the solution
    # This slice copies the list, so we don't append to the actual memoized solutions later
    subproblem_solution = maximum_subarray_helper(arr[:-1], memo)[:]
    subproblem_solution.append(arr[-1])
    subproblem_solution_value = sum(subproblem_solution)

    # alternative solution is to ditch the entire previous array and just use the last element in arr (arr[-1:]).
    alternative_solution = arr[-1:]
    alternative_solution_value = alternative_solution[0]

    # For efficiency, choose the smaller solution if they are equivalent
    if subproblem_solution_value > alternative_solution_value:
        memo[hash_func(arr)] = subproblem_solution
    else:
        memo[hash_func(arr)] = alternative_solution

    solution = memo[hash_func(arr)]

    return solution


class TestMaximumSubarray(unittest.TestCase):
    def test_problem_1(self):
        arr = [1, 2, 3, 4]
        solution = [10, 10]
        self.assertEqual(maximum_subarray_and_subsequence(arr), solution)

    def test_problem_2(self):
        arr = [1]
        solution = [1, 1]
        self.assertEqual(maximum_subarray_and_subsequence(arr), solution)

    def test_problem_3(self):
        arr = [2, -1, 2, 3, 4, -5]
        solution = [10, 11]
        self.assertEqual(maximum_subarray_and_subsequence(arr), solution)

    def test_problem_4(self):
        arr = [-1, -2, -3, -4, -5, -6]
        solution = [-1, -1]
        self.assertEqual(maximum_subarray_and_subsequence(arr), solution)

    def test_problem_5(self):
        arr = [1, -2]
        solution = [1, 1]
        self.assertEqual(maximum_subarray_and_subsequence(arr), solution)

    def test_problem_6(self):
        arr = [1, 2, 3]
        solution = [6, 6]
        self.assertEqual(maximum_subarray_and_subsequence(arr), solution)

    def test_problem_7(self):
        arr = [-10]
        solution = [-10, -10]
        self.assertEqual(maximum_subarray_and_subsequence(arr), solution)

    def test_problem_8(self):
        arr = [1, -1, -1, -1, -1, 5]
        solution = [5, 6]
        self.assertEqual(maximum_subarray_and_subsequence(arr), solution)

    def test_large_set(self):
        with open('./test_data/large_test_data.txt') as file:
            test_cases = int(file.readline())
            for test_case in range(test_cases):
                test_case_size = int(file.readline())
                sys.setrecursionlimit(test_case_size)
                arr_string = file.readline()
                print('test_large_set test case %i, of size %i' % ( test_case, test_case_size))
                arr = [int(x) for x in arr_string.split(' ')]
                my_solution = maximum_subarray_and_subsequence(arr)
                print(str(my_solution))


if __name__ == '__main__':
    unittest.main()
