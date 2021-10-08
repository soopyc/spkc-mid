import turtle


class Helper:
    def __init__(self, _turtle: turtle.Turtle) -> None:
        self.turtle = _turtle

    def move(self, x, y, draw=False) -> None:
        None if draw else self.turtle.penup()
        self.turtle.setpos(x, y)
        None if draw else self.turtle.pendown()

    def move_rel(self, x_rel, y_rel, draw=False) -> None:
        None if draw else self.turtle.penup()
        coord = [self.turtle.xcor(), self.turtle.ycor()]
        coord[0] += x_rel
        coord[1] += y_rel
        print(f'[i] moved to {coord}')
        self.turtle.setpos(*coord)
        None if draw else self.turtle.pendown()

    def rect(self, width, fill='black') -> None:
        init_coord = [self.turtle.xcor(), self.turtle.ycor()]
        init_c = self.turtle.color()
        init_s = self.turtle.shape()
        init_ss = self.turtle.shapesize()
        print(f'[i] init_c = {init_c}, init_s = {init_s}, init_ss = {init_ss}')
        self.turtle.color(fill)
        self.turtle.shapesize(width)
        print(f'[i] current_size = {self.turtle.shapesize()}')
