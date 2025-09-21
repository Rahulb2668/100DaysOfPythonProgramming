from turtle import Turtle


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20

UP=90
RIGHT=0
DOWN=270
LEFT=180

class Snake:
    def __init__(self):
        self.snake_body=[]
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_snake_body(position)

    def add_snake_body(self, position):
        new_segment = Turtle("square")
        new_segment.up()
        new_segment.color("white")
        new_segment.goto(position)
        self.snake_body.append(new_segment)

    def grow(self):
        self.add_snake_body(self.snake_body[-1].pos())

    def move(self):
        for segments in range(len(self.snake_body) - 1, 0, -1):
            next_pos = self.snake_body[segments - 1].pos()
            self.snake_body[segments].goto(next_pos)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for part in self.snake_body:
            part.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


