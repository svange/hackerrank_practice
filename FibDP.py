import unittest
import time

target = 36
ans = 14930352
regular_calls = 0
dp_calls = 0


def fib(n):
    global regular_calls
    regular_calls += 1

    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_dp(n):
    return fib_dp_helper(n, {})


def fib_dp_helper(n, memo):
    global dp_calls
    dp_calls += 1

    if n <= 2:
        return 1

    if memo.get(n - 1):
        fib_n1 = memo[n - 1]
    else:
        fib_n1 = fib_dp_helper(n - 1, memo)
        memo[n - 1] = fib_n1

    if memo.get(n - 2):
        fib_n2 = memo[n - 2]
    else:
        fib_n2 = fib_dp_helper(n - 2, memo)
        memo[n - 2] = fib_n2

    return fib_n1 + fib_n2




class TestFib(unittest.TestCase):
    def SetUp(self):
        global regular_calls
        global dp_calls
        regular_calls = 0
        dp_calls = 0

    def test_fib_dp(self):
        start = time.time()
        solution = fib_dp(target)
        end = time.time()
        print("Calculated fib(%i) = %i in %f seconds, with %i calls" % (target, solution, end - start, dp_calls))
        self.assertEqual(solution, ans)

    def test_fib(self):
        start = time.time()
        solution = fib(target)
        end = time.time()
        print("Calculated fib(%i) = %i in %f seconds, with %i calls" % (target, solution, end - start, regular_calls))
        self.assertEqual(solution, ans)


if __name__ == '__main__':
    unittest.main()
