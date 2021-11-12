import turtle
import time

import player
import food
import logging


class Game:
    BOUNDS = (290, 290, -290, -290)

    def __init__(self):
        self.win = turtle.Screen()
        self.win.bgcolor('green')
        self.win.setup(600, 600)
        self.win.tracer(0)

        self.player = player.Player()
        self.food = food.Food(self.BOUNDS)

    def setup_abort_handler(self):
        def stop():
            logging.debug('removing player turtle')
            self.win.bye()

        self.win.onkeypress(stop, "Escape")
        self.win.onkeypress(stop, "q")

    def bounds_check(self):
        return

    def start(self):
        self.player.setup_listeners(self.win)
        self.setup_abort_handler()
        while True:
            self.win.update()
            self.player.step()

            # Check for collision
            # if self.player.collision(self.food):
            #     score += 1

            # Next iteration
            time.sleep(0.075)


if __name__ == "__main__":
    game = Game()
    game.start()
