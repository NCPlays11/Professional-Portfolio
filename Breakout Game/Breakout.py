import turtle
from turtle import Screen
from game_screen import Game_screen
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
from lives import Life
import time
import tkinter
timer_for_speed_increase = 0

def start_timer():
    global timer_for_speed_increase
    timer_for_speed_increase += 1

def start_game():
    try:
        screen = Screen()
        screen.clear()
        turtle.tracer(0, 0)
        screen.bgcolor("black")
        screen.title("My BreakOut Game")
        screen.setup(width=800, height=600, )
        screen.cv._rootwindow.resizable(False, False)

        g = Game_screen()
        p = Paddle((0, -280))
        b = Ball()
        s = Scoreboard()
        l = Life()

        global timer_for_speed_increase
        floor_hit_count = 5
        g.create_bricks()
        b.ball_movement()
        turtle.getcanvas().bind('<Motion>', p.move_paddle)
        turtle.tracer(1)
        turtle.update()
        should_continue=True
        angle = 0

        while should_continue and floor_hit_count>0 and len(g.bricks) != 0:
            start_timer()

            if timer_for_speed_increase%70==0:
                b.move_speed*=.9
                
            screen.update()
            time.sleep(b.move_speed)
            b.ball_movement()

            if b.xcor()>380 or b.xcor()<-380:
                b.ball_bounce_x()

            if b.ycor()>290:
                b.ball_bounce_y()

            if b.ycor()<-290:
                floor_hit_count-=1
                l.calculate_life(1)
                time.sleep(1)
                b.goto(-100,-285)
                p.goto(0,-280)
                b.move_speed =0.1
                b.ball_bounce_y()
            if p.ycor() - 19 <= b.ycor() <= p.ycor() + 19 and p.xcor() - 55 <= b.xcor() <= p.xcor() + 55 and b.ycor()>-285: ###  paddle hit check
                paddle_middle = p.xcor()
                if b.xcor() < paddle_middle-8:

                    b.ball_bounce_paddle("left")
                elif b.xcor() > paddle_middle+8:

                    b.ball_bounce_paddle("right")
                else:
                    b.ball_bounce_paddle("center")

            angle += 30
            for i in g.bricks:
                if b.distance(i)<50:
                    hit_brick_color=i.color()[0]
                    current_brick_index=g.bricks.index(i)
                    del g.bricks[current_brick_index]
                    i.hideturtle()
                    b.ball_bounce_y()
                    if hit_brick_color=="yellow":
                        s.calculate_score(1)
                    if hit_brick_color=="green":
                        s.calculate_score(3)
                    if hit_brick_color=="orange":
                        s.calculate_score(5)
                    if hit_brick_color=="red":
                        s.calculate_score(10)

        s.reset_score()
        if len(g.bricks)==0:
            b.goto(0, 190)
            b.pendown()
            b.write("Congratulations!", align="center", font=("Helvetica", 24, "bold"))
            time.sleep(2)

    except (turtle.Terminator, tkinter.TclError):

            exit()

start_game()

while True:
    answer = turtle.textinput("Play Again!!","Do you want to play again? Type 'yes' or 'no'")
    if answer is None or answer.lower().startswith('n'):
        break

    else:
        start_game()