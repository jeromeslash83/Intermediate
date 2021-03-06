from turtle import Turtle

class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.score1 = 0
        self.score2 = 0

    def division(self):
        self.penup()
        self.pensize(1)
        self.setposition(0, -300)
        self.setheading(90)
        self.pendown()
        for _ in range(600 // 50):
            self.forward(50 / 2 + 1)
            self.penup()
            self.forward(50 / 2 + 1)
            self.pendown()
        self.penup()
       
    def addscore1(self):
        self.clear()
        self.score1 += 1
    
    def addscore2(self):
        self.clear()
        self.score2 += 1

    def score_1(self):
        self.goto(250, 200)
        self.write(f"Player 1:\n{self.score1}", True, align="center", font=("Arial", 20, 'bold'))

    def score_2(self):
        self.goto(-220, 200)
        self.write(f"Player 2:\n{self.score2}", True, align="center", font=("Arial", 20, 'bold'))

    def winner1(self):
        self.goto(0,0)
        self.write(f"Player 1 Wins", True, align="center", font=("Arial", 20, 'bold'))

    def winner2(self):
        self.goto(0,0)
        self.write(f"Player 2 Wins", True, align="center", font=("Arial", 20, 'bold'))
