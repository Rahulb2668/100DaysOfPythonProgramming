from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def paddle_move(self, direction):
        if direction == "up":
            if self.ycor() < 230:
                new_y = self.ycor() + 20
                self.goto(self.xcor(), new_y)

        if direction == "down":
            if self.ycor() > -230:
                new_y = self.ycor() - 20
                self.goto(self.xcor(), new_y)



