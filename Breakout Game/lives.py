from turtle import Turtle
class Life(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 280)
        self.fillcolor("white")
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.life = 5
        self.update_life()

    def update_life(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Remaining Lives:{self.life}", align='center', font=('Helvetica', 20, 'normal'))
        
    def calculate_life(self,value):
         self.life -=value
         self.update_life()