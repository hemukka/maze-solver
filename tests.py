import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 24
        num_rows = 20
        cell_size = 10
        m1 = Maze(0, 0, num_rows, num_cols, cell_size, cell_size)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        self.assertEqual(
            m1._cells[1][1]._x1,
            cell_size,
        )
        self.assertEqual(
            m1._cells[1][1]._y2,
            cell_size * 2,
        )

    def test_maze_create_cells_margin(self):
        num_cols = 5
        num_rows = 4
        cell_size = 10
        margin = 25
        m1 = Maze(margin, margin, num_rows, num_cols, cell_size, cell_size)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        self.assertEqual(
            m1._cells[1][1]._x1,
            margin + cell_size,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1]._y2,
            margin + cell_size * num_rows,
        )

    def test_maze_create_cells_non_square(self):
        num_cols = 6
        num_rows = 5
        cell_size_x = 10
        cell_size_y = 30
        m1 = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        self.assertEqual(
            m1._cells[1][1]._x1,
            cell_size_x,
        )
        self.assertEqual(
            m1._cells[1][1]._y2,
            cell_size_y * 2,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 11
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[0][0].has_left_wall,
            True,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_right_wall,
            True,
        )

    def test_maze_break_walls(self):
        num_cols = 12
        num_rows = 11
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        # check that all cells have 1 to 3 walls
        # (4-way intersection would have 0 walls,
        # but those don't seem to happen often)
        total_walls = 0
        for i in range(num_cols):
            for j in range(num_rows):
                walls = 0
                if m1._cells[i][j].has_left_wall:
                    walls += 1
                if m1._cells[i][j].has_right_wall:
                    walls += 1
                if m1._cells[i][j].has_top_wall:
                    walls += 1
                if m1._cells[i][j].has_bottom_wall:
                    walls += 1
                self.assertIn(walls, (1,2,3))
                total_walls += walls
        # on average there should be around 1.5 to 2 walls per cell
        walls_min = num_cols * num_rows * 1.5
        walls_max = num_cols * num_rows * 2
        self.assertTrue(walls_min <= total_walls <= walls_max)
        # visited should be reset after breaking walls
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertFalse(m1._cells[i][j].visited)


if __name__ == "__main__":
    unittest.main()