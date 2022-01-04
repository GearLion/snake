# To create the scoreboard
from turtle import Turtle, Screen
ALIGNMENT = 'center'
SCORE_FONT = ("Courier", 12, "normal")
GAME_OVER_FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", mode="r") as past_score:
            self.high_score = int(past_score.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.keep_score()
        self.text_input = Screen()

    def is_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as past_score:
                past_score.write(str(self.high_score))
        self.score = 0

    def keep_score(self):
        self.clear()
        self.setposition(0, 280)
        self.write(arg=f"Score: {self.score}   High Score: {self.high_score}", align=ALIGNMENT, font=SCORE_FONT)

    def snake_scores(self):
        self.score += 1

    def game_over(self):
        self.setposition(-50, 0)
        self.write(arg="GAME OVER", font=GAME_OVER_FONT)

    def play_again(self):
        going = True
        go = self.text_input.textinput(title="Play again?", prompt="Would you like to play again? Type 'yes' or 'no'.").lower()
        while going:
            if go == "yes":
                going = False
                return True
            elif go == "no":
                going = False
                return False
            else:
                go = self.text_input.textinput(title="Play again?", prompt="I'm sorry, but that was an invalid input. Please answer 'yes' or 'no'.").lower()
