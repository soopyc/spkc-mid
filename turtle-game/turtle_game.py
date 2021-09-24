import turtle

lancer = turtle.Turtle()


def move(x, y):
    lancer.penup()
    lancer.setpos(x, y)
    lancer.pendown()


def move_rel(x_rel, y_rel):
    lancer.penup()
    coord = [lancer.xcor(), lancer.ycor()]
    coord[0] += x_rel
    coord[1] += y_rel
    print(f'[i] moved to {coord}')
    lancer.setpos(*coord)
    lancer.pendown()


lancer.color('white', 'pink')
move_rel(0, -100)
lancer.begin_fill()
lancer.circle(150)
lancer.end_fill()

lancer.color('white', 'red')
move_rel(0, 25)
lancer.begin_fill()
lancer.circle(100)
lancer.end_fill()


lancer.penup()
turtle.done()
