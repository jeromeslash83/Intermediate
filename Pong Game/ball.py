from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1, 1)
        self.color("white")
        self.penup()
        self.speed(8)


    def move(self):
        self.fd(20)

    def reset(self):
        self.reset()