import turtle

unit = 5

def pic(c):
    c.forward(unit)
    c.left(45)
    c.forward(unit)
    c.right(90)
    c.forward(unit)
    c.left(45)
    c.forward(unit)

def star(c):
    c.left(60)
    c.forward(unit)

    for i in range(3):
        c.left(60)
        c.forward(unit)
        c.right(120)
        c.forward(unit)

    c.left(60)
    c.forward(unit)
    c.left(60)

def line(c):
    pic(c)
    star(c)
    pic(c)

def side(c):
    line(c)
    c.left(60)
    line(c)
    c.right(120)
    line(c)
    c.left(60)
    line(c)

def snowflake():
    bg = turtle.Screen()
    bg.bgcolor("black")
    c = turtle.Turtle()
    c.color("white")

    for i in range(6):
        side(c)
        c.right(120)
        side(c)
        c.left(60)

    bg.exitonclick()
