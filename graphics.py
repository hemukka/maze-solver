from tkinter import Tk, BOTH, Canvas

class Point():
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1:Point, point2:Point):
        self.start = point1
        self.end = point2

    def draw(self, canvas:Canvas, fill_color:str="black"):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y,
            fill=fill_color, width=2
            )

class Window():
    def __init__(self, width:int, height:int):
        self.__root = Tk()
        self.__root.title("Maze solver")
        # self.__root.geometry(f"{width}x{height}")

        self.__canvas = Canvas(self.__root, height=height, width=width, bg="white" )
        self.__canvas.pack(fill=BOTH, expand=True)

        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False

    def draw_line(self, line:Line, fill_color:str="black"):
        line.draw(self.__canvas, fill_color)

