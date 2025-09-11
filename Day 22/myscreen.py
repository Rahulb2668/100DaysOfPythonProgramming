from turtle import Screen

class MyScreen:
    def __init__(self, dimensions):
        self.screen = Screen()
        self.screen.setup(dimensions[0], dimensions[1])
        self.screen.bgcolor("black")
        self.screen.title("Pong")
        self.screen.tracer(0)
        self.screen.listen()

    def listen(self):
        self.screen.listen()

    def onkeypress (self, func, key):
        self.screen.onkeypress(func, key)

    def update(self):
        self.screen.update()

    def exitonclick(self):
        self.screen.exitonclick()

