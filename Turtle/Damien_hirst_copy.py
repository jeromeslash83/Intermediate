from turtle import Turtle, Screen
import turtle as tu
import random

t = Turtle(visible=True)
t.penup()
t.setheading(270)
t.fd(200)
t.setheading(180)
t.fd(200)
tu.colormode(255)
t.pendown()
t.setheading(0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def move_forward():
    for _ in range(11):
        t.pencolor(random_color())
        t.dot(20)
        t.penup()
        t.fd(40)
        t.pendown()

def move_up():
    t.penup()
    t.left(90)
    t.fd(40)
    t.left(90)
    t.fd(440)
    t.setheading(0)

for _ in range(11):
    move_forward()
    move_up()
