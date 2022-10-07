import turtle

t=turtle.Turtle()
t.pensize(3)
t.color("green")
t.screen.bgcolor("black")
t.hideturtle()

x=0
y=-140
t.penup()
t.goto(x,y)
t.pendown()
t.circle(140)
t.penup()
t.home()
y=-100
t.goto(x,y)
t.pendown()
t.color("blue")
t.circle(100)
t.penup()
t.home()
t.left(60)

def clock(h,m,s,t):
    for i in range(12):
        t.forward(120)
        t.right(30)
        t.color("yellow")
        t.write((i + 1))
        t.goto(0,0)
    t.pendown()

    #hour
    t.penup()
    t.home()
    t.setheading(90)
    angle=(h/12)*360
    t.right(angle)
    t.color("red")
    t.pensize(3)
    t.pendown()
    t.forward(60)

    # minute
    t.penup()
    t.home()
    t.setheading(90)
    angle = (m / 60) * 360
    t.right(angle)
    t.color("gold")
    t.pensize(2)
    t.pendown()
    t.forward(80)

    # second
    a = 1
    an: int= 0
    c: int=1
    while a > 0:
        if an == 0 or an > 0:
            t.penup()
            t.setheading(90)
            angle = (s / 60) * 360
            t.right(angle+an)
            t.color("green")
            t.pensize(1)
            t.pendown()
            t.forward(73)
            t.undo()
            t.goto(0,0)
            an+=6

            c=s+c
            if c%60==0:
                m=m+1

                if m%60==0:
                    h=h+1

clock(10,55,26,t)
turtle.done()