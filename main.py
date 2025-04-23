from graphics import Window, Point, Line
from cell import Cell

def main():
    win = Window(800, 600)

    # draw test lines
    # win.draw_line(Line(Point(10,10), Point(600, 500)), "red")
    # win.draw_line(Line(Point(500,30), Point(50, 550)), "black")
    # win.draw_line(Line(Point(400,30), Point(50, 50)), )

    # draw test cells
    cells = [
        Cell(10,20,10,20,win),
        Cell(50,60,50,60,win),
        Cell(100,120,100,120,win),
        Cell(150,160,150,160,win),
        Cell(250,260,250,260,win),
    ]
    cells[0].has_bottom_wall = False
    cells[1].has_top_wall = False
    cells[2].has_left_wall = False
    cells[3].has_right_wall = False
    for cell in cells:
        cell.draw()

    win.wait_for_close()

if __name__ == "__main__":
    main()