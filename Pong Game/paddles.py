from turtle import Turtle
import time

class Paddle():
    
    def __init__(self):
        self.paddle_1 = []
        self.paddle_2 = []
        self.first_player()
        self.second_player()
    
    def first_player(self):
        paddle = Turtle(shape="square")
        paddle.speed(0)
        paddle.turtlesize(stretch_len=5)
        paddle.color("sky blue")
        paddle.penup()
        paddle.goto(350, 0)
        paddle.setheading(90)
        self.paddle_1.append(paddle)


    def second_player(self):
        paddle = Turtle(shape="square")
        paddle.speed(0)
        paddle.turtlesize(stretch_len=5)
        paddle.color("sky blue")
        paddle.penup()
        paddle.goto(-350, 0)
        paddle.setheading(90)
        self.paddle_2.append(paddle)

    def move_up_1(self):
        self.paddle_1[0].fd(20)
    

    def move_down_1(self):
        y = self.paddle_1[0].ycor()
        self.paddle_1[0].goto(self.paddle_1[0].xcor(), y - 20)



    def move_up_2(self):
        self.paddle_2[0].fd(20)


    def move_down_2(self):
        y = self.paddle_2[0].ycor()
        self.paddle_2[0].goto(self.paddle_2[0].xcor(), y - 20)

