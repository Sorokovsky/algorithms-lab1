from turtle import *


def setup_settings():
    pen()
    reset()
    down()
    pensize(3)
    speed(.3)
    shape("turtle")
    color("yellow")
    setup(1000, 1000)
    bgcolor("darkGreen")
    title("Спадання висот")
    colormode(255)




setup_settings()
draw_lines()
exitonclick()
