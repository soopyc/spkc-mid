import random
import turtle


class Food:
    def __init__(self, bounds):
        self.turtle: turtle.Turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.bounds = (bounds[0]-5, bounds[1]-5, bounds[2]-5, bounds[3]-5)

    def new_location(self):
        new_coord = (random.randint(self.bounds[0], self.bounds[1]),
                     random.randint(self.bounds[2], self.bounds[3]))
