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


def draw_lines():
    max = 200
    min = 10
    for i in range(max, min - 1, -int(max / min)):
        penup()
        goto(-i, i)
        pendown()
        goto(-i, 0)


setup_settings()
draw_lines()
exitonclick()
