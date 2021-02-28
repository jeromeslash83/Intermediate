from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.score = 0

    def add_score(self):
        self.clear()
        self.score += 1
    
    def scoreboard(self):
        self.goto(0, 275)
        self.write(f"Score: {self.score}", True, align="center", font=("EightBit Atari-Regular", 15, 'bold'))

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", True, align="center", font=("EightBit Atari-Regular", 15, 'bold'))
