from turtle import Turtle, Screen
from random import randint

colors = ['red', 'dark orange', 'gold', 'green', 'blue', 'indigo', 'violet']
y = -150
race_starting = False
screen = Screen()
screen.setup(width=500, height=400)
color_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race?\n('red', 'dark orange', 'gold', 'green', 'blue', 'indigo', 'violet')\nEnter a color: ")
race_turtles = []


for index in range(0, 7):
    turtles = Turtle(shape='turtle')
    turtles.color(colors[index])
    turtles.penup()
    turtles.goto(x=-230,y=y)
    y += 50
    race_turtles.append(turtles)

if color_bet:
    race_starting = True

while race_starting:
    for turtle in race_turtles:
        if turtle.xcor() > 230:
            race_starting = False
            if turtle.pencolor == color_bet:
                screen.textinput(title="win", prompt=f"You win! The winner is {color_bet}.Type OK to exit.")
            else:
                screen.textinput(title="Lose", prompt=(f"You lose. The winner is {turtle.pencolor()}. Type OK to exit."))

        turtle.fd(randint(0, 15))
        



screen.exitonclick()
