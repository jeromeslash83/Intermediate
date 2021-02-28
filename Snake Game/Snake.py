#Snake OOP
from turtle import Turtle
STARTING_COORDINATES = [(0,0), (-20,0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.the_snake = []
        self.snake(STARTING_COORDINATES)
        self.snake_head = self.the_snake[0]

    def snake(self, coordinate):
        for _ in range(3):
            snakes = Turtle(shape="square")
            snakes.color("green")
            snakes.penup()
            snakes.goto(coordinate[_])
            self.the_snake.append(snakes)

    def add_length(self):
            pos = self.the_snake[-1].pos()
            snakes = Turtle(shape="square")
            snakes.color("green")
            snakes.penup()
            snakes.speed(0)
            snakes.goto(pos)
            self.the_snake.append(snakes)
            
    def move(self):
        for segment in range(len(self.the_snake) - 1, 0, -1):
            movementx = self.the_snake[segment - 1].xcor()
            movementy = self.the_snake[segment - 1].ycor()
            self.the_snake[segment].goto(movementx, movementy)
        self.snake_head.fd(20)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
    
    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)


            
