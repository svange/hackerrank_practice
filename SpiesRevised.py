import unittest
from typing import Tuple, List, NamedTuple, Optional
from collections import namedtuple
from itertools import product
from itertools import combinations


class Board:
    def __init__(self, n: int):
        self.n = n
        self.spies = []
        self.spy = namedtuple('Spy', ['x', 'y'])
        self.square = namedtuple('Square', ('x', 'y'))

    def push_spy(self, x: int, y: int):
        if self.spy_count >= self.n:
            raise IndexError()
        if x >= self.n or y >= self.n:
            raise IndexError()
        self.spies.append(self.spy(x, y))

    def peek_spy(self):
        return self.spies[-1]

    def pop_spy(self):
        return self.spies.pop()

    def get_all_spies_except(self, spy):
        return (_spy for _spy in self.spies if _spy.x != spy[0] and _spy.y != spy[1])

    @property
    def spy_count(self):
        return len(self.spies)

    @property
    def is_valid(self):
        if self.do_two_spies_break_the_rules():
            return False
        if self.do_three_spies_break_the_rules():
            return False
        return True

    @staticmethod
    def are_spies_on_horizontal(spy_1, spy_2):
        if spy_1[1] == spy_2[1]:
            return True
        else:
            return False

    @staticmethod
    def are_spies_on_vertical(spy_1: Tuple[int, int], spy_2: Tuple[int, int]):
        if spy_1[0] == spy_2[0]:
            return True
        else:
            return False

    @staticmethod
    def are_spies_on_diagonal(spy_1, spy_2):
        if spy_1[0] - spy_2[0] == spy_1[1] - spy_2[1]:
            return True
        else:
            return False

    def do_two_spies_break_the_rules(self):
        newest_spy = self.spies[-1]
        for existing_spy in self.spies[:-1]:
            if existing_spy == newest_spy:
                continue
            if self.are_spies_on_diagonal(existing_spy, newest_spy):
                return True
            if self.are_spies_on_horizontal(existing_spy, newest_spy):
                return True
            if self.are_spies_on_diagonal(existing_spy, newest_spy):
                return True
            return False

    def do_three_spies_break_the_rules(self):
        newest_spy = self.spies[-1]
        for spy_1, spy_2 in combinations(self.spies[:-1], 2):
            if self.are_spies_on_line(spy_1, spy_2, newest_spy):
                return True
            else:
                return False

    def are_spies_on_line(self, spy_1, spy_2, spy_3):
        pass

    def squares(self, start: Optional[int] = 0, end: Optional[int] = 0):
        return (self.square(x, y) for x, y in product(range(self.n), range(self.n)) if x >= start and y >= end)

    @staticmethod
    def generate_solution(n: int):
        board = Board(n)
        squares = board.squares()

        current_spy = 1
        while current_spy <= n:
            for current_square in squares:
                board.push_spy(current_square.x, current_square.y)
                if board.is_valid:
                    current_spy += 1
                    break
                else:
                    board.pop_spy()
            else:
                board.pop_spy()
                last_spy = board.peek_spy()
                current_spy -= 1
                squares = board.squares(last_spy.x, last_spy.y)
        return board.spies


class TestBoard(unittest.TestCase):
    def test_generate_solution_1_to_10(self):
        pass


if __name__ == '__main__':
    for n in range(1, 11):
        solution = Board.generate_solution(n)
        print('Board size: %i x %i' % (n, n))
        print(str(solution) + '\n')

