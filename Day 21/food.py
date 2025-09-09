from turtle import Turtle
import random

def return_randomxy():
    return (random.randint(-280, 280), random.randint(-280, 280))

class Food (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh_food()


    def refresh_food(self):
        self.goto(return_randomxy())