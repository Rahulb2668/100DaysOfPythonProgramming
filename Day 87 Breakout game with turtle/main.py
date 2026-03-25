import time

from Game import Game

game = Game()

while True:
    time.sleep(0.1)
    game.screen.update()
    game.ball.move()
    if game.ball.xcor() > 165 or game.ball.xcor() < -170:
        game.ball.bounce_x()

    if game.ball.ycor() > 220:
        game.ball.bounce_y()

    if game.ball.ycor() < -230:
        game.scoreboard.reset_score()
        time.sleep(2)
        game.ball.goto(0, 0)
        game.ball.bounce_y()


    if game.ball.distance(game.paddle) < 35 and game.ball.ycor() < -210:
        game.ball.bounce_y()

    for brick in game.all_bricks[:]:
        if game.ball.distance(brick) < 30:
            brick.hideturtle()
            game.all_bricks.remove(brick)
            game.ball.bounce_y()
            game.scoreboard.increase_score()
            break