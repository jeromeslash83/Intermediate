#Main
from turtle import Turtle, Screen
import random



screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jslash Snake Game")


snake_pos = [(0,0),(-20,0),(-40,0)]
for position in snake_pos:
    snake = Turtle(shape="square")
    snake.color("green")
    snake.goto(position)

