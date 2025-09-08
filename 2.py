from turtle import *
from random import randint

width = 400
height = 400


def setup_settings():
    reset()
    pensize(3)
    speed(3)
    shape("turtle")
    color("blue", "green")
    setup(width, height)
    bgcolor("lightGreen")
    title("Різнокольорові кулі")
    penup()
    colormode(255)


def draw_random_circle():
    max_radius = 100
    x = randint(-width // 2 + max_radius, width // 2 - max_radius)
    y = randint(-height // 2 + max_radius, height // 2 - max_radius)
    radius = randint(10, max_radius)

    circle_color = (randint(0, 255), randint(0, 255), randint(0, 255))

    goto(x, y)

    color(circle_color)
    fillcolor(circle_color)

    pendown()
    begin_fill()
    circle(radius)
    end_fill()
    penup()


setup_settings()

for _ in range(5):
    draw_random_circle()

exitonclick()