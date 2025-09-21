from turtle import Turtle

SCORE_STYLE = ('Arial', 14, 'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.highScore=0
        self.pencolor("white")
        self.setpos(0, 280)
        self.hideturtle()
        self.read_high_score()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highScore}" , move=False, font=SCORE_STYLE, align="center")

    def update_score(self):
        self.score+=1
        self.write_score()

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
        self.score = 0
        self.write_score()
        self.write_high_score()

    def read_high_score(self):
        with open("data.txt") as file:
            score = file.read()
            if score != "":
                self.highScore = int(score)
            else:
                self.highScore = 0


    def write_high_score(self):
        with open ("data.txt", "w") as file:
            file.write(str(self.highScore))



    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", move=False , font=SCORE_STYLE, align="Center")