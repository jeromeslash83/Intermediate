#Main Code
import time
from turtle import Screen, Turtle
from Snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jslash Snake Game")
screen.tracer(0)

snake = Snake()

snake_is_alive = True
while snake_is_alive:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
