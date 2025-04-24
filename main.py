from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    num_rows = 10
    num_cols = 12
    margin = 50
    screen_width = 800
    screen_height = 600
    cell_width = (screen_width - 2 * margin) / num_cols
    cell_height = (screen_height - 2 * margin) / num_rows
    win = Window(screen_width, screen_height)

    # draw test lines
    # win.draw_line(Line(Point(10,10), Point(600, 500)), "red")
    # win.draw_line(Line(Point(500,30), Point(50, 550)), "black")
    # win.draw_line(Line(Point(400,30), Point(50, 50)), )

    # draw test cells
    # cells = [
    #     Cell(10,20,10,20,win),
    #     Cell(50,60,50,60,win),
    #     Cell(100,120,100,120,win),
    #     Cell(150,160,150,160,win),
    #     Cell(250,260,250,260,win),
    # ]
    # cells[0].has_bottom_wall = False
    # cells[1].has_top_wall = False
    # cells[2].has_left_wall = False
    # cells[3].has_right_wall = False
    # for cell in cells:
    #     cell.draw()
    # cells[0].draw_move(cells[1])
    # cells[2].draw_move(cells[3], True)

    maze = Maze(margin, margin, num_rows, num_cols, cell_width, cell_height, win)
    print("maze created")
    if maze.solve():
        print("maze solved")
    win.wait_for_close()

if __name__ == "__main__":
    main()