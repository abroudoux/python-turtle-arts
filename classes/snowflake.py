class Snowflake:
    def __init__(self, bg, c):
        self.unit = 5
        self.c = c
        self.bg = bg

    def pic(self):
        self.c.forward(self.unit)
        self.c.left(45)
        self.c.forward(self.unit)
        self.c.right(90)
        self.c.forward(self.unit)
        self.c.left(45)
        self.c.forward(self.unit)

    def star(self):
        self.c.left(60)
        self.c.forward(self.unit)

        for i in range(3):
            self.c.left(60)
            self.c.forward(self.unit)
            self.c.right(120)
            self.c.forward(self.unit)

        self.c.left(60)
        self.c.forward(self.unit)
        self.c.left(60)

    def line(self):
        self.pic()
        self.star()
        self.pic()

    def side(self):
        self.line()
        self.c.left(60)
        self.line()
        self.c.right(120)
        self.line()
        self.c.left(60)
        self.line()

    def draw(self):
        for i in range(6):
            self.side()
            self.c.right(120)
            self.side()
            self.c.left(60)

        self.bg.exitonclick()
