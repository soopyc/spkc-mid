import turtle

import logging


class Player:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.shape('square')
        self.turtle.color('black')
        self.turtle.penup()
        self.turtle.goto(0, 0)
        self.direction = "stop"

    def _setup_listeners(self, win: turtle.TurtleScreen):
        win.listen()
        win.onkeypress(self.up, "Up")
        win.onkeypress(self.down, "Down")
        win.onkeypress(self.left, "Left")
        win.onkeypress(self.right, "Right")

    def up(self):
        if self.direction == 'down':
            logging.debug("Cannot move up, ignoring request")
            return
        self.direction = 'up'

    def down(self):
        if self.direction == 'up':
            logging.debug("Cannot move down, ignoring request")
            return
        self.direction = 'up'

    def left(self):
        if self.direction == 'right':
            logging.debug("Cannot move left, ignoring request")
            return
        self.direction = 'up'

    def right(self):
        if self.direction == 'left':
            logging.debug("Cannot move right, ignoring request")
            return
        self.direction = 'up'

    @staticmethod
    def _add_coors(x, y, tx, ty):
        return x + tx, y + ty

    def collision(self, item):
        return self.turtle.distance(item) <= 20

    def step(self):
        _movements = {
            'up': (0, 20),
            'down': (0, -20),
            'left': (20, 0),
            'right': (-20, 0),
            'stop': (0, 0)
        }
        coord = (self.turtle.xcor(), self.turtle.ycor())
        new_coord = self._add_coors(*coord, *_movements.get(self.direction))
        logging.debug(f"Current: {coord}, moving to {new_coord}")
        self.turtle.goto(new_coord)
