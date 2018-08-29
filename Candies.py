import unittest


class Teacher:
    def __init__(self, score_arr):
        self._score_array = score_arr
        self._calculated_cost = None

    @property
    def score_array(self):
        return self._score_array

    @score_array.setter
    def score_array(self, candy_arr):
        self._score_array = candy_arr

    @property
    def calculated_cost(self):
        if self._calculated_cost is not None:
            return self._calculated_cost
        else:
            self._calculated_cost = self._least_candy_calculation()
            return self._calculated_cost

    def _least_candy_calculation(self):
        candy_arr = [1]
        for i in range(len(self.score_array))[1::]:
            prev_score = self.score_array[i - 1]
            curr_score = self.score_array[i]

            if curr_score > prev_score:
                # curr position deserves more candy
                candy_arr.append(candy_arr[i - 1] + 1)
            elif curr_score <= prev_score:
                # curr position deserves less candy
                candy_arr.append(1)
                j = i
                while self.score_array[j] < self.score_array[j - 1] and candy_arr[j - 1] <= candy_arr[j]:
                    candy_arr[j - 1] = candy_arr[j] + 1
                    j -= 1
                    if j == 0:
                        break
        return sum(candy_arr)

class TestStringMethods(unittest.TestCase):

    def test_basic(self):
        solution = Teacher([2, 4, 2, 6, 1, 7, 8, 9, 2, 1])
        self.assertEqual(19, solution.calculated_cost)

if __name__ == '__main__':
    unittest.main()

