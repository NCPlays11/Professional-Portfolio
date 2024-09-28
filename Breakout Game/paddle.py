from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()

        self.penup()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=7,stretch_len=1)
        self.setheading(90)
        self.goto(position)

    def move_paddle(self,event):
        x = event.x - 400
        if x < -390:
            x = -390
        elif x > 390:
            x = 390
        self.goto(x, self.ycor())