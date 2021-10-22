import logging
import turtle


class Score:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.color('white')
        self.turtle.penup()
        self.turtle.hideturtle()

        self.high_score = 0
        self.turtle.goto(0, 260)

    def draw_score(self, score: int):
        logging.debug(f'Writing score {score}')
        self.turtle.write(f"Score: {score}\nHigh Score: {self.high_score}",
                          align="center", font=("Courier", 24, "normal"))
