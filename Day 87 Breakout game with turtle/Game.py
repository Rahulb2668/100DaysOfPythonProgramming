from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from Bricks import Brick
from ScoreBoard import Scoreboard

class Game:
    def __init__(self):
        self.screen = Screen()
        self.paddle = Paddle()
        self.ball = Ball()
        self.all_bricks = []
        self.scoreboard = Scoreboard()

        cv = self.screen.getcanvas()
        cv.winfo_toplevel().resizable(False, False)

        # Screen or window configuration
        self.screen.setup(400, 500)
        self.screen.bgcolor('black')
        self.screen.title('Breakout')
        self.screen.tracer(0)
        self.screen.listen()

        self.screen.onkeypress(self.paddle.move_left, key="Left")
        self.screen.onkeypress(self.paddle.move_right, key='Right')
        self.generate_bricks()
    def generate_bricks(self):
        for r in range(3):
            for c in range (10):
                x_pos = -180 + (c * 42)
                y_pos = 200 - (r * 22)
                new_brick = Brick((x_pos, y_pos))
                self.all_bricks.append(new_brick)
