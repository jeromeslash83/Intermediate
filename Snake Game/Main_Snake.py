#Main Code
import time
from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jslash Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

snake_is_alive = True
while snake_is_alive:
    score.scoreboard()
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.add_length()
        score.add_score()
    
    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() > 290  or snake.snake_head.ycor() < -290:
        snake_is_alive = False
        score.gameover()

    for snake_part in snake.the_snake:
        if snake_part == snake.snake_head:
            pass
        elif snake.snake_head.distance(snake_part) < 10:
            snake_is_alive = False
            score.gameover()

screen.exitonclick()
