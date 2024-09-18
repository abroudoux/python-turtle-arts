class Spirale:
    def __init__(self, bg, c):
        self.unit = 10
        self.c = c
        self.bg = bg

    def square(self, c):
        for i in range(4):
            c.forward(self.unit)
            c.left(90)

    def draw(self):
        for i in range(100):
            self.square(self.c)
            self.c.left(15)
            self.unit += i / 10

        self.bg.exitonclick()