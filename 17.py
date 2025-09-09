from turtle import *


def setup_settings():
    pen()
    reset()
    down()
    pensize(3)
    speed(.3)
    shape("turtle")
    color("blue")
    setup(1000, 1000)
    bgcolor("yellow")
    title("Вкладані квадрати")
    colormode(255)


def draw_squares_decreasing():
    for i in range(200, 0, -20):
        penup()
        goto(-i / 2, i / 2)
        pendown()
        for _ in range(4):
            forward(i)
            right(90)


def erase_squares_increasing():
    color((224, 172, 105))
    for i in range(20, 201, 20):
        penup()
        goto(-i / 2, i / 2)
        pendown()
        for _ in range(4):
            forward(i)
            right(90)


setup_settings()
draw_squares_decreasing()
erase_squares_increasing()
exitonclick()
