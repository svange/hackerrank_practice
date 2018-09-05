import unittest
import os


def grid_challenge():
    pass


class TestGridChallenge(unittest.TestCase):

    @staticmethod
    def get_test_cases(fptr):
        ###
        # MODIFY HERE ACCORDING TO THE OUTPUT FILE RULES
        ###
        num_test_cases = int(fptr.readline())
        test_cases = []
        for test_case in range(num_test_cases):
            lines = int(fptr.readline())
            test_cases.append([])
            for line in range(lines):
                test_cases[test_case].append(fptr.readline())
        return test_cases

    @staticmethod
    def get_solutions(fptr):
        ###
        # MODIFY HERE ACCORDING TO THE INPUT FILE RULES
        ###
        solutions = []
        for line in fptr:
            solutions.append(line)
        return solutions

    def test_samples(self):
        path_to_test_input_files = './test_data/GridChallenge/input'
        path_to_test_output_files = './test_data/GridChallenge/output'

        for in_file, out_file in zip(os.listdir(path_to_test_input_files), os.listdir(path_to_test_output_files)):
            with open(path_to_test_input_files + '/' + in_file, 'r') as in_fptr, \
                    open(path_to_test_output_files + '/' + out_file, 'r') as out_fptr:

                test_cases = self.get_test_cases(in_fptr)
                solutions = self.get_solutions(out_fptr)

                for test, solution, num in zip(test_cases, solutions, range(len(test_cases))):
                    with self.subTest(msg="input: %s\noutput: %s\ntest_case: %i" % (in_file, out_file, num)):
                        print('hi')
                        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
