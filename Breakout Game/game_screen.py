from turtle import Turtle
class Game_screen():

    def __init__(self):
        self.bricks = []
        self.colours=["yellow","green","orange","red"]
        
    def create_bricks(self):
        x=-375
        y=0
        for j in range(4):
            for k in range(2):
                for i in range(10):
                    tim = Turtle()
                    tim.penup()
                    tim.setheading(90)
                    self.bricks.append(tim)
                    tim.shape("square")
                    tim.color(self.colours[j])
                    tim.shapesize(stretch_len=.8, stretch_wid=3.5)
                    tim.goto(x, y)
                    tim.speed(0)
                    x= x + 80
                y+=25
                x=-375
