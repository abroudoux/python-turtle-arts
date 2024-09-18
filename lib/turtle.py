import turtle

class Turtle:
    def __init__(self):
        bg = turtle.Screen()
        bg.bgcolor("black")
        c = turtle.Turtle()
        c.color("white")

        self.bg = bg
        self.c = c

    def get_config(self):
        return self.bg, self.c