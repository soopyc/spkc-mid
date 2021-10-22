import turtle
import time

import player


class Game:
    BOUNDS = (290, 290, -290, -290)

    def __init__(self):
        self.win = turtle.Screen()
        self.win.bgcolor('green')
        self.win.setup(600, 600)
        self.win.tracer(0)

        self.player = player.Player()

    def bounds_check(self):
        return

    def start(self):
        while True:
            self.win.update()
            self.player.step()

            # Check for collision
            if self.player.collision():
                score = 1

            # Next iteration
            time.sleep(0.2)


if __name__ == "__main__":
    game = Game()
    game.start()