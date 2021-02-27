#Snake OOP
from turtle import Turtle
STARTING_COORDINATES = [(0,0), (-20,0), (-40, 0)]

class Snake:

    def __init__(self):
        self.the_snake = []
        self.snake(STARTING_COORDINATES)


    def snake(self, coordinate):
        for _ in range(3):
            snakes = Turtle(shape="square")
            snakes.color("green")
            snakes.penup()
            snakes.goto(coordinate[_])
            self.the_snake.append(snakes)


    def move(self):
        for segment in range(len(self.the_snake) - 1, 0, -1):
            movementx = self.the_snake[segment - 1].xcor()
            movementy = self.the_snake[segment - 1].ycor()
            self.the_snake[segment].goto(movementx, movementy)
        self.the_snake[0].fd(20)
            
