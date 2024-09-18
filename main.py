from classes.snowflake import Snowflake
from classes.spirale import Spirale
from classes.trinity import Trinity
from lib.turtle import Turtle

if __name__ == '__main__':
    bg, c = Turtle().get_config()

    # Snowflake(bg, c).draw()
    # Spirale(bg, c).draw()
    Trinity(bg, c).draw()
