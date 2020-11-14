import random as r
import turtle as t

import base as b
imporstate = {'score': 0}
path = t.Turtle(visible=False)
writer = t.Turtle(visible=False)

aim = b.vector(5, 0)
pacman = b.vector(-40, 80)

ghosts = [

    [b.vector(-180, 160), b.vector(5, 0)],

    [b.vector(-180, 160), b.vector(0, 5)],

    [b.vector(100, 160), b.vector(0, -5)],

    [b.vector(100, -160), b.vector(-5, 0)]

]

tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]


def square(x, y):
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()


def offset(point):
    x = (b.floor(point.x, 20) + 200) / 20

    y = (180 - b.floor(point.y, 20)) / 20

    index = int(x + y * 20)

    return index


def valid(point):
    index = offset(point)

    if tiles[index] == 0:
        return False
    index = offset(point + 19)
    if tiles[index] == 0:
        return False
    return point.x % 20 == 0 or point.y % 20 == 0


def world():
    t.bgcolor("black")
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]
        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')


def move():
    writer.undo()
    writer.write(state['score'])
    t.clear()
    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)
    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)
    t.up()
    t.goto(pacman.x + 10, pacman.y + 10)
    t.dot(20, 'yellow')

    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            options = [
                b.vector(5, 0),
                b.vector(-5, 0),
                b.vector(0, 5),
                b.vector(0, -5)

            ]
            plan = r.choice(options)
            course.x = plan.x
            course.y = plan.y

        t.up()
        t.goto(point.x + 10, point.y + 10)
        t.dot(20, 'red')
    t.update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    t.ontimer(move, 100)


def change(x, y):
    if valid(pacman + b.vector(x, y)):
        aim.x = x
        aim.y = y


t.setup(420, 420, 370, 0)
t.hideturtle()
t.tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
t.listen()
t.onkey(lambda: change(5, 0), 'Right')
t.onkey(lambda: change(-5, 0), 'Left')
t.onkey(lambda: change(0, 5), 'Up')
t.onkey(lambda: change(0, -5), 'Down')
world()
move()
t.done()
