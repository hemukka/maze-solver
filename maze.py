from time import sleep

from cell import Cell
from graphics import Window

class Maze():
    def __init__(self,
                 x1:int,
                 y1:int,
                 num_rows:int,
                 num_cols:int,
                 cell_size_x:int,
                 cell_size_y:int,
                 win:Window=None
                 ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for i in range(self._num_cols):
            self._cells.append([])
            for j in range(self._num_rows):
                x1 = self._x1 + (self._cell_size_x * i)
                x2 = x1 + self._cell_size_x
                y1 = self._y1 + (self._cell_size_y * j)
                y2 = y1 + self._cell_size_y
                self._cells[i].append(Cell(x1, x2, y1, y2, self._win))
                self._draw_cell(i, j)

    def _draw_cell(self, i:int, j:int):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(-1, -1)