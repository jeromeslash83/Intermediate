from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
from board import Board
import random
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Jerome's Pong Game")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
ball.speed(8)
player_1 = paddle.paddle_1[0]
player_2 = paddle.paddle_2[0]
score = Board()

screen.listen()
screen.onkey(paddle.move_up_1, "Up")
screen.onkey(paddle.move_down_1, "Down")
screen.onkey(paddle.move_up_2, "w")
screen.onkey(paddle.move_down_2, "s")


game_is_ongoing = True
while game_is_ongoing:
    score.division()
    score.score_1()
    score.score_2()
    screen.update() 
    time.sleep(0.1)








    
    




screen.exitonclick()