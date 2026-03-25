from turtle import *
PADDLE_POS_X = 0
PADDLE_POS_Y = -230


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_len=2, stretch_wid=0.5)
        self.penup()
        self.goto(PADDLE_POS_X, PADDLE_POS_Y)

    def move_left(self):
        if self.xcor() > -165:
            self.setx(self.xcor() - 20)

    def move_right(self):
        if self.xcor() < 160:
            self.setx(self.xcor() + 20)