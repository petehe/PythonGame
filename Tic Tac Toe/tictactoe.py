import turtle as t
import base as b


def grid():
    b.line(-67, 200, -67, -200)
    b.line(67, 200, 67, -200)
    b.line(-200, -67, 200, -67)
    b.line(-200, 67, 200, 67)


def drawx(x, y):
    b.line(x, y, x + 133, y + 133)
    b.line(x, y + 133, x + 133, y)


def drawo(x, y):
    t.up()
    t.goto(x + 67, y + 5)
    t.down()
    t.circle(62)


def floor(value):
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    t.update()
    state['player'] = not player


t.setup(420, 420, 370, 0)
t.hideturtle()
t.tracer(False)
grid()
t.update()
t.onscreenclick(tap)
t.done()
