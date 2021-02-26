#Main
from turtle import Turtle, Screen
import random
import time

screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jslash Snake Game")
screen.tracer(0)

x = 0
the_snake = []
for _ in range(3):
    snake = Turtle(shape="square")
    snake.color("green")
    snake.penup()
    snake.goto(x=x, y=0)
    x -= 20
    the_snake.append(snake)

snake_moving = True

while snake_moving:
    for segment in the_snake:
        segment.fd(20)
        screen.update()

