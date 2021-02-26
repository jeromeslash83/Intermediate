#Main
from turtle import Turtle, Screen
import random



screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jslash Snake Game")

x = 0
the_snake = []
for _ in range(3):
    snake = Turtle(shape="square")
    snake.color("green")
    snake.goto(x=x, y=0)
    x -= 20
    the_snake.append(snake)

