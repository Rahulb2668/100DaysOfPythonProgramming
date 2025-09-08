import random
import turtle as t

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
turtle_colors= ["violet", "indigo", "blue", "yellow", "orange", "red", "green"]

user_guess = screen.textinput(title="Make your guess", prompt="Input the color of the turtle you bet on:  ").lower()
all_turtles = []

if user_guess:
    is_race_on = True

for turtle_index in range(7):
    new_turtle = t.Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(turtle_colors[turtle_index])
    new_turtle.goto(x=-230, y=-100 + turtle_index * 30)
    all_turtles.append(new_turtle)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_guess:
                print(f"{turtle.pencolor()} You Won" )
            else:
                print(f"{turtle.pencolor()} You Fail")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()