import turtle

from turtle import Turtle,Screen
ALIGNMENT="center"
FONT=("Arial", 20, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.upgrade_score()

    def upgrade_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.color("red")
        self.goto(0,0)
        self.write('GAME OVER!', align=ALIGNMENT, font=FONT)




    def increase_score(self):
        self.score += 1
        self.clear()
        self.upgrade_score()