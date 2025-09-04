import turtle as t

tim = t.Turtle()


for sides in range(3, 10):
    for _ in range(sides):
        tim.forward(100)
        tim.right(360/sides)
t.mainloop()