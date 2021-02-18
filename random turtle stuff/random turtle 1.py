from turtle import Turtle, Screen
import turtle as tu
import random

t = Turtle()
tu.colormode(255)
t.speed(0)

def random_color():
    r = random.choice(range(1, 255))
    g = random.choice(range(1, 255))
    b = random.choice(range(1, 255))
    return (r, g, b)


def draw_square():
    for _ in range(4):
        t.fd(200)
        t.right(90)

for angle in range(0, 360, 3):
    t.setheading(angle)
    t.pencolor(random_color())
    draw_square()




screen = Screen()
screen.exitonclick()
