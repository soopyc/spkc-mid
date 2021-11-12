# score.py: score display
import logging
import turtle


class Score:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.color('white')
        self.turtle.penup()
        self.turtle.hideturtle()

        self.score = 0
        self.high_score = 0
        self.turtle.goto(0, 260)

    def draw_score(self):
        logging.debug(f'Writing score {self.score}')
        self.turtle.write(f"Score: {self.score}\nHigh Score: {self.high_score}",
                          align="center", font=("Courier", 24, "normal"))
        logging.debug(f"Checking if score is higher than high score...")
        if self.score >= self.high_score:
            logging.info(f"Saving score {self.score} as high-score")
        else:
            logging.debug("Not saving high score.")

    def add_score(self, score):
        self.score += score
        return self.score
