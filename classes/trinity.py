class Trinity:
    def __init__(self, bg, c):
        self.unit = 500
        self.c = c
        self.bg = bg

        self.c.right(45)

    def triangle(self):
        for i in range(3):
            self.c.forward(self.unit)
            self.c.right(120)

    def fill_triangle(self, n):
        self.c.forward(self.unit)
        self.c.right(120)
        self.c.forward(self.unit / n)
        self.c.right(120)
        self.c.forward(self.unit / n)
        self.c.left(120)
        self.c.forward(self.unit / n)
        self.c.left(120)
        self.c.forward(self.unit / n)

    def draw(self):
        self.triangle()
        self.fill_triangle(2)

        self.c.right(120)
        self.c.forward(self.unit / 2)
        self.c.right(120)
        self.c.forward(self.unit)
        self.c.right(120)

        self.fill_triangle(4)

        self.bg.exitonclick()