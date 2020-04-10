import os
from time import sleep
from .cell import Cell

class Board:
    
    def __init__(self, num_rows: int, num_cols: int, matrix: list = None) -> None:
        self._cycles = 0
        self._nrows = num_rows
        self._ncols = num_cols
        self._board = [[Cell() for j in range(self._ncols)] for i in range(self._nrows)]
        if matrix and self._is_correct_shape(matrix):
            for i in range(self._nrows):
                for j in range(self._ncols):
                    if matrix[i][j]:
                        self._board[i][j] = Cell(is_alive=True)
                    else:
                        self._board[i][j] = Cell()

    def __str__(self) -> None:
        result = ''
        for i in range(self._nrows):
            for j in range(self._ncols):
                result += (str(self._board[i][j]))
                result += ' ' if j < self._ncols - 1 else ''
            result += '\n' if i < self._nrows - 1 else ''
        return result

    def calculate_next_board_state(self) -> None:
        new_state = [[False for j in range(self._ncols)] for i in range(self._nrows)]
        # calculate the next state for each index
        for i in range(self._nrows):
            for j in range(self._ncols):
                new_state[i][j] = self.calculate_next_state_for_index(i,j)
        self.set_new_state(new_state)
        self._cycles += 1

    def calculate_next_state_for_index(self, i: int, j: int) -> bool:
        neighbors = self.get_neighbors_for_index(i, j)
        live_count = len([n for n in neighbors if n.is_alive])
        if live_count < 2 or live_count > 3:
            return False
        else:
            if not self._board[i][j].is_alive and live_count == 2:
                return False
            else:
                return True

    # determines neighbors given index including edge cases
    def get_neighbors_for_index(self, i: int, j: int) -> list:
        if i == 0:
            if j == 0:
                return [
                    self._board[i][j + 1],
                    self._board[i + 1][j],
                    self._board[i + 1][j + 1]
                ]
            elif j == len(self._board[0]) - 1:
                return [
                    self._board[i][j - 1],
                    self._board[i + 1][j - 1],
                    self._board[i + 1][j],
                ]
            else:
                return [
                    self._board[i][j - 1],
                    self._board[i][j + 1],
                    self._board[i + 1][j - 1],
                    self._board[i + 1][j],
                    self._board[i + 1][j + 1]
                ]
        elif i == len(self._board) - 1:
            if j == 0:
                return [
                    self._board[i - 1][j],
                    self._board[i - 1][j + 1],
                    self._board[i][j + 1],
                ]
            elif j == len(self._board[0]) - 1:
                return [
                    self._board[i - 1][j - 1],
                    self._board[i - 1][j],
                    self._board[i][j - 1],
                ]
            else:
                return [
                    self._board[i - 1][j - 1],
                    self._board[i - 1][j],
                    self._board[i - 1][j + 1],
                    self._board[i][j - 1],
                    self._board[i][j + 1],
                ]
        else:
            if j == 0:
                return [
                    self._board[i - 1][j],
                    self._board[i - 1][j + 1],
                    self._board[i][j + 1],
                    self._board[i + 1][j],
                    self._board[i + 1][j + 1]
                ]   
            elif j == len(self._board[0]) - 1:
                return [
                    self._board[i - 1][j - 1],
                    self._board[i - 1][j],
                    self._board[i][j - 1],
                    self._board[i + 1][j - 1],
                    self._board[i + 1][j],
                ]
            else:
                return[
                    self._board[i - 1][j - 1],
                    self._board[i - 1][j],
                    self._board[i - 1][j + 1],
                    self._board[i][j - 1],
                    self._board[i][j + 1],
                    self._board[i + 1][j - 1],
                    self._board[i + 1][j],
                    self._board[i + 1][j + 1]
                ]
        

    def set_new_state(self, new_state: list) -> None:
        if self._is_correct_shape(new_state):
            for i in range(len(new_state)):
                for j in range((len(new_state[0]))):
                    if new_state[i][j]:
                        self._board[i][j].live()
                    else:
                        self._board[i][j].die()
        
    # validation helper for setting new state
    def _is_correct_shape(self, new_state: list) -> bool:
        if len(new_state) != self._nrows:
            raise Exception('new state does not match number of rows')
        
        for row in range(len(new_state)):
            if len(new_state[row]) != self._ncols:
                raise Exception('new state does not match number of columns')
        
        return True

    # TODO
    def liven_at_index(self, row: int, col: int) -> None:
        self._board[row][col].die()

    # TODO
    def kill_at_index(self, row: int, col: int) -> None:
        self._board[row][col].live()

    def play(self) -> None:
        while True:
            self.calculate_next_board_state()
            print('CYCLE: ', self._cycles)
            print('\n')
            print(self.__str__())
            sleep(0.2)
            os.system('cls' if os.name == 'nt' else 'clear')

