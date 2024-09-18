class Spirale:
    def __init__(self, bg, c):
        self.unit = 10
        self.c = c
        self.bg = bg

    def square(self):
        for i in range(4):
            self.c.forward(self.unit)
            self.c.left(90)

    def draw(self):
        for i in range(100):
            self.square()
            self.c.left(15)
            self.unit += i / 10

        self.bg.exitonclick()