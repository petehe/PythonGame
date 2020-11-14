import turtle as t
state = {'turn': 0}


def spinner():
    t.clear()
    angle = state['turn'] / 10

    t.right(angle)
    t.forward(100)

    t.dot(120, "red")
    t.back(100)
    t.right(120)
    t.forward(100)

    t.dot(120, 'green')
    t.back(100)
    t.right(120)
    t.forward(100)

    t.dot(120, 'blue')
    t.back(100)
    t.right(120)
    t.update()


def animate():
    if state['turn']:
        state['turn'] -= 1
    spinner()
    t.ontimer(animate, 20)


def flick():
    state['turn'] += 10
t.setup(420,420,370,0)
t.hideturtle()
t.tracer(False)
t.width(20)
t.onkey(flick,'space')
t.listen()
animate()
t.done()
