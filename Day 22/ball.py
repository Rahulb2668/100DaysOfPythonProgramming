import random
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.dx = 10
        self.dy = 10
        self.move_speed=0.1

    def create_ball(self):
        self.shape("circle")
        self.penup()
        self.color("white")

    def move(self):
        self.goto(self.xcor()+ self.dx, self.ycor()+ self.dy)


    def y_bounce(self):
        self.dy *= -1

    def x_bounce(self, screen_dimensions=None):
        self.move_speed*=.9
        self.dx *= -1

    def check_y_collision(self, screen_dimensions=None):
        if screen_dimensions is None:
            screen_dimensions = [800, 600]
        height_threshold = screen_dimensions[1]/2 - 30
        if self.ycor() > height_threshold or self.ycor() < -height_threshold:
            self.y_bounce()

    def check_x_collision(self, screen_dimensions=None, update_score=None):
        if screen_dimensions is None:
            screen_dimensions = [800, 600]
        width_threshold = screen_dimensions[0] / 2 - 20
        if self.xcor() > width_threshold:
            if callable(update_score):
                update_score("l")
            self.goto(0, 0)
            self.x_bounce()
            self.move_speed = 0.1
        elif self.xcor() < -width_threshold:
            if callable(update_score):
                update_score("r")
            self.goto(0, 0)
            self.x_bounce()
            self.move_speed=0.1