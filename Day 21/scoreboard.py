from turtle import Turtle

SCORE_STYLE = ('Arial', 14, 'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.pencolor("white")
        self.setpos(0, 280)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", move=False, font=SCORE_STYLE, align="center")

    def update_score(self):
        self.clear()
        self.score+=1
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", move=False , font=SCORE_STYLE, align="Center")