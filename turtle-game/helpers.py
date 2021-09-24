class Helper:
    def __init__(self, turtle):
        self.turtle = turtle

    def move(self, x, y, draw=False):
        None if draw else self.turtle.penup()
        self.turtle.setpos(x, y)
        None if draw else self.turtle.pendown()

    def move_rel(self, x_rel, y_rel, draw=False):
        None if draw else self.turtle.penup()
        coord = [self.turtle.xcor(), self.turtle.ycor()]
        coord[0] += x_rel
        coord[1] += y_rel
        print(f'[i] moved to {coord}')
        self.turtle.setpos(*coord)
        None if draw else self.turtle.pendown()

    def rect(self, length, width, fill='black'):
        self.move_rel()
