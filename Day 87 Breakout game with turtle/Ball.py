from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0,0)
        self.movex = 10
        self.movey = 10

    def move(self):
        new_x = self.xcor() + self.movex
        new_y = self.ycor() + self.movey
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.movey *= -1

    def bounce_x(self):
        self.movex *= -1