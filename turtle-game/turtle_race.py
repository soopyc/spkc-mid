import turtle
import time
import random

from helpers import Helper

wn = turtle.Screen()
tur = turtle.Turtle()
helper = Helper(tur)

wn.title('Turtle Racing')
wn.bgcolor("lightblue")
tur.color("white")
tur.hideturtle()

tur.speed(5)
helper.move_rel(-150, 200)
tur.color("#4c5576")
tur.write("Turtle Game", font=('Comic Sans MS', 30, 'bold'))
helper.move(0, 0)
tur.showturtle()

helper.rect(5, 5, 'black')

turtle.done()
