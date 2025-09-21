import time
from turtle import Screen

from scoreboard import ScoreBoard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

game_not_over = True

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# Initial sleep time (slower speed)
base_sleep_time = 0.1
# Minimum sleep time (fastest speed)
min_sleep_time = 0.05
# Speed increase per food eaten (adjust as needed)
speed_increment = 0.005

while game_not_over:
    current_sleep_time = max(min_sleep_time, base_sleep_time - (score_board.score * speed_increment))
    time.sleep(current_sleep_time)
    snake.move()
    screen.update()

    if snake.head.distance(food) < 15:
        food.refresh_food()
        score_board.update_score()
        snake.grow()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    for part in snake.snake_body[3:]:
        if snake.head.distance(part) < 10:
            score_board.reset()
            snake.reset()


screen.exitonclick()