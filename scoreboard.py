# To create the scoreboard
from turtle import Turtle
ALIGNMENT = 'center'
SCORE_FONT = ("Courier", 12, "normal")
GAME_OVER_FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.setposition(0, 280)
        self.hideturtle()
        self.keep_score()

    def keep_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=SCORE_FONT)
        self.score += 1

    def game_over(self):
        self.setposition(-50, 0)
        self.write(arg="GAME OVER", font=GAME_OVER_FONT)
