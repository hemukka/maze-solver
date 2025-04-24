from graphics import Point, Line, Window
from typing import Self

class Cell():
    def __init__(self, x1:int, x2:int, y1:int, y2:int, window:Window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = window

    def draw(self):
        if self._win is None:
            return
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1),
                                     Point(self._x1, self._y2)))
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1),
                                    Point(self._x2, self._y2)))
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1),
                                    Point(self._x2, self._y1)))
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2),
                                    Point(self._x2, self._y2)))
    
    def draw_move(self, to_cell:Self, undo:bool=False):
        if self._win is None:
            return
        line_color = "red" 
        if undo:
            line_color = "grey"
        self._win.draw_line(Line(Point((self._x1 + self._x2) / 2,
                                       (self._y1 + self._y2) / 2),                                 
                                 Point((to_cell._x1 + to_cell._x2) / 2,
                                       (to_cell._y1 + to_cell._y2) / 2)),
                                line_color)
        