import random
import turtle
import base


def value():
    return (3 + random.random() * 2) * random.choice([-1, 1])


ball = base.vector(0, 0)
aim = base.vector(value(), value())


def draw():
    ball.move(aim)
    x = ball.x
    y = ball.y

    z = ball.x + ball.y


    if x < -200 or x > 200:
        aim.x = -aim.x
    if y < -200 or y > 200:
        aim.y = -aim.y
    turtle.clear()
    turtle.goto(x, y)
    turtle.dot(10, "blue")
    turtle.ontimer(draw, 50)


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.up()
draw()
turtle.done()
