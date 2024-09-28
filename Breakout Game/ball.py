from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(-150, -300)
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1

    def ball_movement(self):
        x=self.xcor()+self.x_move
        y=self.ycor()+self.y_move
        self.goto(x,y)

    def ball_bounce_x(self):
            self.x_move*=-1

    def ball_bounce_y(self):
         self.y_move*=-1

    def ball_bounce_brick(self):
        self.y_move*=1

    def ball_bounce_paddle(self,side):
        if side=="left":
            if self.x_move == 0:
                self.x_move = 10
            if  self.xcor()<0:
                if self.x_move>0:
                    self.x_move *= -1
                else:
                    self.x_move*=1
            else:
                if self.x_move>0:
                    self.x_move *= -1
                else:
                    self.x_move*=1

            self.y_move*=-1

        elif side =="right":
            if self.x_move == 0:
                self.x_move = 10
            if self.xcor() > 0:
                if self.x_move<0:
                    self.x_move *= -1
                else:
                    self.x_move*=1

            else:
                if self.x_move<0:
                    self.x_move *= -1
                else:
                    self.x_move*=1
            self.y_move*=-1

        else:
            # print(self.xcor(),self.ycor())
            self.y_move*=-1
            self.x_move*=0