import functools
from math import factorial


def solve(arr):
    if len(arr) <= 1:
        return 0

    tallest = max(arr)
    num_tallest = arr.count(tallest)

    if num_tallest <= 1:
        tallest_paths = 0
    else:
        tallest_paths = factorial(num_tallest) / factorial(num_tallest - 2)

    splits = [i for i, x in enumerate(arr) if x == tallest]

    arrs = []
    current = 0
    for split in splits:
        arrs.append(arr[current:split])
        current = split + 1

    sub_problem_answers = map(solve, arrs)
    sum_sub_problem_answers = functools.reduce(lambda x, y: x + y, sub_problem_answers)

    return int(tallest_paths + sum_sub_problem_answers)



if __name__ == '__main__':
    arr_1 = [1, 1, 1, 2, 2]  # 8
    arr_2 = [3, 2, 1]  # 0
    arr_3 = [1, 2, 3] # 0
    arr_4 = [3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3]  # 14

    arrs = [arr_1, arr_2, arr_3, arr_4]

    for arr in arrs:
        print(solve(arr))