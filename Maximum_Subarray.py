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
    maximum_subarray_value = maximum_subarray_helper(arr)
    # Find the subarray with the solution of max value
    return maximum_subarray_value


def maximum_subarray_helper(arr):
    if len(arr) == 1:
        return arr[0]

    # lists of length 1 are easy
    # these are the properties for a subarray of length 1 starting at 0
    last_solution = max_solution = arr[0]

    # loop through all subarrays starting at 0
    # keep track of last solution (to use in next iteration)
    # keep track of max solution to return at end of method
    for end in range(2, len(arr) + 1):
        # subproblem is finding the maximum_subarray of arr[:-1]
        # subproblem_solution is the solution of subproblem with the last item of arr appended to the solution
        subproblem_solution_value = last_solution + arr[end - 1]

        # alternative solution is to ditch the entire previous array and just use the last element in arr (arr[-1:]).
        alternative_solution_value = arr[end - 1]

        # update last_solution
        if subproblem_solution_value > alternative_solution_value:
            last_solution = subproblem_solution_value
        else:
            last_solution = alternative_solution_value
        max_solution = max((max_solution, last_solution))

    solution = max_solution

    return solution


####################
# IGNORE THIS METHOD,
# NOT USED,
# JUST SAVING IT
# FOR NO GOOD REASON
####################
def maximum_subarray_helper_recursive(arr, memo):
    # Alias for readability
    # lists are mutable -> lists are not hashable
    # tuples are mutable -> tuples are hashable
    def hash_func(_arr):
        return str(tuple(_arr))

    # subarrays of len 0 or 1 are their own solutions
    # base case
    if len(arr) <= 1:
        # keys for memo are
        if len(arr) == 0:
            memo[hash_func(arr)] = 0
            return 0
        else:
            memo[hash_func(arr)] = arr[0]
            return arr[0]

    # subproblem is finding the maximum_subarray of arr[:-1]
    # subproblem_solution is the solution of subproblem with the last item of arr appended to the solution
    # This slice copies the list, so we don't append to the actual memoized solutions later
    if memo.get(hash_func(arr[:-1])):
        subproblem_solution_value = memo.get(hash_func(arr[:-1])) + arr[-1]
    else:
        subproblem_solution_value = maximum_subarray_helper_recursive(arr[:-1], memo) + arr[-1]

    # alternative solution is to ditch the entire previous array and just use the last element in arr (arr[-1:]).
    alternative_solution_value = arr[-1]

    if subproblem_solution_value > alternative_solution_value:
        memo[hash_func(arr)] = subproblem_solution_value
    else:
        memo[hash_func(arr)] = alternative_solution_value

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
        solutions = {
            0: [2617065, 172083036],
            1: [1274115, 193037987],
            2: [2202862, 163398048],
            3: [2454939, 240462364],
            4: [3239908, 186256172],
            5: [2486039, 202399661],
            6: [1092777, 137409985],
            7: [962621, 135978139],
            8: [3020911, 224370860],
            9: [1755033, 158953999]
        }
        with open('./test_data/maximum_subarray/large_test_data.txt') as file:
            test_cases = int(file.readline())
            for test_case in range(test_cases):
                test_case_size = int(file.readline())
                print("Testing list of size " + str(test_case_size))
                arr_string = file.readline()
                arr = [int(x) for x in arr_string.split(' ')]
                my_solution = maximum_subarray_and_subsequence(arr)
                self.assertEqual(my_solution, solutions[test_case])


if __name__ == '__main__':
    unittest.main()
