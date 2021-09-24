import turtle

from helpers import Helper

wn = turtle.Screen()
tur = turtle.Turtle()
helper = Helper(tur)

wn.title('Turtle Racing')
wn.bgcolor("lightblue")
tur.color("white")
tur.ht()

tur.speed(0)
helper.move_rel(-150, 200)
tur.color("pink")
tur.write("Turtle Game", font=('Comic Sans MS', 30, 'bold'))


turtle.done()
