from turtle import *
from random import uniform
import math

width = 400
height = 400

def setup_window():
    reset()
    speed(.5)
    setup(width, height)
    bgcolor("lightgreen")
    title("Перетин кіл")
    colormode(255)
    penup()

def draw_circle(cx, cy, radius, color_rgb):
    goto(cx, cy - radius)
    setheading(0)
    pendown()
    color(color_rgb)
    circle(radius)
    penup()

def draw_group(theta_deg, radiuses):
    group_color = (
        int(uniform(0, 1) * 255),
        int(uniform(0, 1) * 255),
        int(uniform(0, 1) * 255)
    )
    theta_rad = math.radians(theta_deg)
    for r in radiuses:
        cx = r * math.cos(theta_rad)
        cy = r * math.sin(theta_rad)
        draw_circle(cx, cy, r, group_color)

radii = [5, 10, 15, 20, 25, 30, 35, 40]

setup_window()

for group in range(4):
    theta = group * 90
    draw_group(theta, radii)

exitonclick()