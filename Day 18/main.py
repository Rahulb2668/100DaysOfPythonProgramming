import random
import turtle as t

tim = t.Turtle()
t.colormode(255)

tim.speed("fastest")

def get_color():
    return random.randint(1, 255), random.randint(1, 255),random.randint(1, 255)

def draw_spirogram(gap):
    for _ in range(int(360/gap)):
        current_heading = tim.heading()
        tim.color(get_color())
        tim.circle(100)
        tim.setheading(current_heading+gap)


draw_spirogram(10)


t.mainloop()