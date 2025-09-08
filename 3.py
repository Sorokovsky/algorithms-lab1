from turtle import *
from random import uniform
import math

width = 400
height = 400

def setup_window():
    reset()
    speed(10)
    setup(width, height)
    bgcolor("purple")
    title("Квітка")
    penup()
    colormode(255)

def draw_petal(x, y, radius, color_rgb):
    goto(x, y)
    pendown()
    color(color_rgb)
    fillcolor(color_rgb)
    begin_fill()
    circle(radius)
    end_fill()
    penup()

def draw_flower(num_petals=7):
    center_x, center_y = 0, 0
    petal_radius = 30
    distance_from_center = 30
    angle_step = 360 / num_petals

    for i in range(num_petals):
        angle = math.radians(i * angle_step)
        x = center_x + distance_from_center * math.cos(angle)
        y = center_y + distance_from_center * math.sin(angle)
        petal_color = (
            int(uniform(0, 1) * 255),
            int(uniform(0, 1) * 255),
            int(uniform(0, 1) * 255)
        )
        draw_petal(x, y, petal_radius, petal_color)

    center_radius = 25
    center_color = (
        int(uniform(0, 1) * 255),
        int(uniform(0, 1) * 255),
        int(uniform(0, 1) * 255)
    )
    draw_petal(center_x, center_y, center_radius, center_color)

setup_window()
draw_flower()
exitonclick()