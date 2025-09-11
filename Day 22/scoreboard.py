from turtle import Turtle

SCORE_STYLE = ('Arial', 14, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.pencolor("white")
        self.setpos(0, 280)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.write(f"{self.l_score} ------ {self.r_score}", move=False , font=SCORE_STYLE,align="center")


    def update_score(self, who):
        self.clear()
        if who == "r":
            self.r_score += 1
        else:
            self.l_score += 1
        self.write(f"{self.l_score} ------ {self.r_score}", move=False, font=SCORE_STYLE, align="center")
