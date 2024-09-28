from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.goto(0, 280)
        self.fillcolor("white")
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        with open(file="score_tracking.txt") as ft:
            self.high_score=ft.read()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(200, 250)
        self.write(f"Highest Score:{self.high_score}\nYour Score:{self.score}", align='center', font=('Helvetica', 12, 'normal'))
    def calculate_score(self,value):
         self.score +=value
         self.update_score()
    def reset_score(self):
        if self.score > int(self.high_score):
            self.high_score=self.score
            with open("score_tracking.txt",mode="w") as ft:
                ft.write(f"{self.high_score}")