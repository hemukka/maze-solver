from time import sleep
import random

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
                 win:Window=None,
                 seed:int=None
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

        if seed:
            random.seed(seed)
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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

    def _animate(self, sleep_time:int=0.01):
        if self._win is None:
            return
        self._win.redraw()
        sleep(sleep_time)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(-1, -1)

    def _break_walls_r(self, i:int, j:int):
        """ Break walls by depth-first search and randomly picked direction """
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i - 1 >= 0 and self._cells[i - 1][j].visited == False:
                to_visit.append((i - 1, j))
            if i + 1 < self._num_cols and self._cells[i + 1][j].visited == False:
                to_visit.append((i + 1, j))
            if j - 1 >= 0 and self._cells[i][j - 1].visited == False:
                to_visit.append((i, j - 1))
            if j + 1 < self._num_rows and self._cells[i][j + 1].visited == False:
                to_visit.append((i, j + 1))
            if not to_visit:
                self._draw_cell(i, j)
                return
            next = to_visit[random.randrange(len(to_visit))]
            if next[0] < i:
                self._cells[i][j].has_left_wall = False
                self._cells[next[0]][next[1]].has_right_wall = False
            if next[0] > i:
                self._cells[i][j].has_right_wall = False
                self._cells[next[0]][next[1]].has_left_wall = False
            if next[1] < j:
                self._cells[i][j].has_top_wall = False
                self._cells[next[0]][next[1]].has_bottom_wall = False
            if next[1] > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[next[0]][next[1]].has_top_wall = False
            # self._draw_cell(i, j)
            # self._draw_cell(next[0], next[1])
            self._break_walls_r(next[0], next[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        """ Find path through the maze with depth-first search.
         Return True if end was found
         """
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate(0.05)
        cell:Cell = self._cells[i][j]
        cell.visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        if i > 0 and not cell.has_left_wall and not self._cells[i-1][j].visited:
            cell.draw_move(self._cells[i-1][j])
            if self._solve_r(i - 1, j):
                return True
            cell.draw_move(self._cells[i-1][j], undo=True)
        if i + 1 < self._num_cols and not cell.has_right_wall and not self._cells[i+1][j].visited:
            cell.draw_move(self._cells[i+1][j])
            if self._solve_r(i + 1, j):
                return True
            cell.draw_move(self._cells[i+1][j], undo=True)
        if j > 0 and not cell.has_top_wall and not self._cells[i][j-1].visited:
            cell.draw_move(self._cells[i][j-1])
            if self._solve_r(i, j - 1):
                return True
            cell.draw_move(self._cells[i][j-1], undo=True)
        if j + 1 < self._num_rows and not cell.has_bottom_wall and not self._cells[i][j+1].visited:
            cell.draw_move(self._cells[i][j+1])
            if self._solve_r(i, j + 1):
                return True
            cell.draw_move(self._cells[i][j+1], undo=True)
        return False
