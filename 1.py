from turtle import *


def setup_window():
    pen()
    reset()
    down()
    pensize(3)
    speed(3)
    shape("turtle")
    color('blue', 'green')
    setup(400, 400)
    bgcolor('yellow')
    title("Квадрати й усі вказівки")
    begin_fill()


def draw_square():
    for i in range(1, 5):
        forward(100)
        dot()
        left(90)
    end_fill()
    for i in range(1, 5):
        color("cyan")
        backward(100)
        color("red")
        dot()
        right(90)
        up()
        goto(-180, 150)
        color("red")
        write("Намалювали два квадрати")
        goto(-120, 130)
        color("DarkViolet")
        write('і продемонстрували роботу вказівок')
        goto(0, 0)
        shape("classic")
        exitonclick()


setup_window()
draw_square()
