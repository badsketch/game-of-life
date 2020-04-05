class CellState:
    DEAD = '◻'
    ALIVE = '◼︎'

class Cell:

    def __init__(self, is_alive=False):
        self._is_alive = is_alive

    def __str__(self):
        if self._is_alive:
            return CellState.ALIVE
        else:
            return CellState.DEAD

    @property
    def is_alive(self):
        return self._is_alive

    def die(self):
        self._is_alive = False

    def live(self):
        self._is_alive = True