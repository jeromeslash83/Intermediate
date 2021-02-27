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

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

snake_is_alive = True
while snake_is_alive:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
