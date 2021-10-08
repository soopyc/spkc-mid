import turtle
import random
import time


class Game:
    def __init__(self):
        self.win = turtle.Screen()
        self.win.bgcolor('green')
        self.win.setup(600, 600)
        self.win.tracer(0)

        self.player = turtle.Turtle()
        self.player.speed(0)
        self.player.shape('square')
        self.player.color('black')
        self.player.penup()
        self.player.goto(0, 0)
        self.player.direction = "stop"

    def p_up(self):
        if self.player.direction == "down":
            print('[i] ')
        self.player.direction = "up"
