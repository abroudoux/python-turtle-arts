import turtle

from snowflake import Snowflake
from spirale import Spirale

if __name__ == '__main__':
    bg = turtle.Screen()
    bg.bgcolor("black")
    c = turtle.Turtle()
    c.color("white")

    Snowflake(bg, c).draw()
    # Spirale(bg, c).draw()
