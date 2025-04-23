from graphics import Window, Point, Line

def main():
    win = Window(800, 600)

    # draw test lines
    win.draw_line(Line(Point(10,10), Point(600, 500)), "red")
    win.draw_line(Line(Point(500,30), Point(50, 550)), "black")
    win.draw_line(Line(Point(400,30), Point(50, 50)), )

    win.wait_for_close()

if __name__ == "__main__":
    main()