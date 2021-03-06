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

initial_ball_heading = [45, 135, 225, 315, 30, 120, 210, 300, 60, 150, 240, 330]
game_is_ongoing = True
while game_is_ongoing:
    score.division()
    score.score_1()
    score.score_2()
    screen.update() 
    time.sleep(0.1)
    if ball.position() == (0,0):
        ball.setheading(random.choice(initial_ball_heading))
        ball.color("white")
        ball.penup()
    ball.move()

    if ball.xcor() > 380:
        score.addscore2()
        ball.goto(0,0)
    elif ball.xcor() < -380:
        score.addscore1()
        ball.goto(0,0)
    elif ball.ycor() > 280 or ball.ycor() < -280:
        ball.setheading(-ball.heading())
    elif player_1.distance(ball) < 30:
        ball.setheading(180 - ball.heading())
        ball.move()
    elif player_2.distance(ball) < 30:
        ball.setheading(180 - ball.heading())
        ball.move()
    
    if score.score1 = 5 or score.score2 = 5:
        


         
    







    
    




screen.exitonclick()