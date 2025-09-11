import time

from myscreen import MyScreen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

SCREEN_DIMENSION  = [800, 600]
screen = MyScreen(dimensions=SCREEN_DIMENSION)
scoreboard = ScoreBoard()
game_over = False


paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
ball.move()

screen.onkeypress(lambda : paddle_left.paddle_move("up"), "w")
screen.onkeypress(lambda: paddle_left.paddle_move("down"), "s")
screen.onkeypress(lambda: paddle_right.paddle_move("up"), "Up")
screen.onkeypress(lambda: paddle_right.paddle_move("down"), "Down")
screen.onkeypress(screen.screen.bye, "q")

while not game_over:
    time.sleep(ball.move_speed)
    ball.move()
    ball.check_y_collision(screen_dimensions=SCREEN_DIMENSION)
    ball.check_x_collision(screen_dimensions=SCREEN_DIMENSION, update_score=scoreboard.update_score)

    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320 :
        ball.x_bounce()

    screen.update()

screen.exitonclick()
