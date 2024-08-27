import turtle
from datetime import datetime

t = turtle.Turtle()
t.pensize(7)
t.color("green")
t.screen.bgcolor("black")

t.hideturtle()
x = 0
y = -140
t.penup()
t.goto(x, y)
t.pendown()
t.circle(140)
t.penup()
t.home()
y = -100
t.goto(x, y)
t.pendown()
t.pensize(5)
t.color("blue")
t.circle(100)
t.penup()
t.home()
t.left(60)


def fun_hr(h):
    t.penup()
    t.home()
    t.setheading(90)
    angle = (h / 12) * 360
    t.right(angle)
    t.pensize(4)
    t.pendown()
    t.forward(60)


def fun_min(m):
    t.penup()
    t.home()
    t.setheading(90)
    angle = (m / 60) * 360
    t.right(angle)
    t.pensize(3)
    t.pendown()
    t.forward(80)
    t.penup()
    t.goto(0, 0)


def clock(h, m, s, t):
    for i in range(12):
        t.forward(120)
        t.right(30)
        t.color("yellow")
        t.write((i + 1))
        t.goto(0, 0)
    t.pendown()

    # hour
    t.color("red")
    fun_hr(h)

    # minute
    t.color("gold")
    fun_min(m)

    # second
    a = 1

    while a > 0:
        t.speed(6)
        t.setheading(90)
        angle = (s / 60) * 360
        t.right(angle)
        t.color("green")
        t.pensize(2)
        t.forward(73)
        t.pendown()
        t.undo()
        t.color("black")
        t.penup()
        t.goto(0, 0)
        s += 1

        if s % 60 == 0:
            m1=m+1
            t.color("black")
            fun_min(m)
            t.color("gold")
            fun_min(m1)
            m=m1

            if m1 % 60 == 0:
                h1 = h + 1
                t.color("black")
                fun_hr(h)
                t.color("red")
                fun_hr(h1)
                h=h1
        t.pendown()


now = datetime.now()
hour = now.hour
minute = now.minute
second = now.second

clock(hour, minute, second, t)

turtle.done()
