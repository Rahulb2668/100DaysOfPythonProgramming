from turtle import Turtle

from sqlalchemy.sql.operators import truediv

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setpos(STARTING_POSITION)
        self.setheading(90)


    def move(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def won(self):
        if self.ycor() >= 280:
            return True
        else:
            return False