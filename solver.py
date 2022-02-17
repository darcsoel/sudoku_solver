from typing import List, Type

from validator import Validator


class Solver:
    def __init__(self, board: List[List[str]], validator: Type[Validator]):
        if not validator(board).is_valid():
            raise ValueError("Board is not valid")

        self.board = board

    def solve(self):
        pass
