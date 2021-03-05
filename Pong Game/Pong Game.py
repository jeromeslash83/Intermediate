from turtle import Turtle, Screen
from paddles import Paddle
import time


screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Jerome's Pong Game")
screen.tracer(0)



paddle = Paddle()

screen.listen()
screen.onkey(paddle.move_up_1, "Up")
screen.onkey(paddle.move_down_1, "Down")
screen.onkey(paddle.move_up_2, "w")
screen.onkey(paddle.move_down_2, "s")


game_is_ongoing = True
while game_is_ongoing:
    screen.update()
    time.sleep(0.1)





screen.exitonclick()
