from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.fd(10)

def clockwise():
    tim.right(10)

def move_backwards():
    tim.bk(10)

def counter_clockwise():
    tim.left(10)

screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=counter_clockwise)
screen.onkeypress(key="d", fun=clockwise)
screen.onkeypress(key="c", fun=screen.reset)




screen.exitonclick()
