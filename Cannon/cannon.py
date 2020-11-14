import random
import turtle

import base

ball = base.vector(-200, -200)
speed = base.vector(0, 0)
targets = []


def inside(xy):
    return -200 < xy.x < 200 and -200 < xy.y < 200


def tap(x, y):
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def draw():
    turtle.clear()
    for target in targets:
        turtle.goto(target.x, target.y)
        turtle.dot(20, "blue")
    if inside(ball):
        turtle.goto(ball.x, ball.y)
        turtle.dot(6, "red")

    turtle.update()


def move():
    if random.randrange(40) == 0:
        y = random.randrange(-150, 150)
        target = base.vector(20, y)
        targets.append(target)
    for target in targets:
        target.x -= 0.5
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)
    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
    draw()

    for target in targets:
        if not inside(target):
            return
    turtle.ontimer(move, 50)

turtle.setup(420,420,370,0)
turtle.hideturtle()
turtle.up()
turtle.tracer(False)
turtle.onscreenclick(tap)
move()
turtle.done()
