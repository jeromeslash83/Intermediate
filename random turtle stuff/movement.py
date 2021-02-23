from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.setheading(0)
    tim.fd(10)

def move_backwards():
    tim.setheading(180)
    tim.fd(10)

def move_up():
    tim.setheading(90)
    tim.fd(10)

def move_down():
    tim.setheading(270)
    tim.fd(10)

screen.listen()
screen.onkey(key="Right", fun=move_forwards)
screen.onkey(key="Left", fun=move_backwards)
screen.onkey(key="Up", fun=move_up)
screen.onkey(key="Down", fun=move_down)




screen.exitonclick()
