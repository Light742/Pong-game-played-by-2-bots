from turtle import Turtle, Screen
from UserPlank import UserPlank
from CPUPlank import CpuPlank
from pong import Pong
import time
from scoreboard import ScoreBoard

contact = 0
diff_user = 0
diff_cpu = 0
divider = Turtle()
screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
divider.hideturtle()
divider.goto(0, 300)
divider.pencolor("white")
divider.setheading(270)
divider.pensize(5)
for i in range(20):
    divider.forward(20)
    divider.penup()
    divider.forward(20)
    divider.pendown()

user_plank = UserPlank()
cpu_plank = CpuPlank()
pong = Pong()
user_score = ScoreBoard(-200, 200)
cpu_score = ScoreBoard(200, 200)
cpu_score.scoreboard()
user_score.scoreboard()
screen.listen()
screen.onkeypress(key="w", fun=user_plank.move_up)
screen.onkeypress(key="s", fun=user_plank.move_down)
screen.onkeypress(key="i", fun=cpu_plank.move_up)
screen.onkeypress(key="k", fun=cpu_plank.move_down)

game_on = True

while game_on:
    screen.update()
    time.sleep(0.01)
    pong.initial_motion()
    prev_angle_y = 0
    prev_angle_x = 0
    cpu_plank.goto(350, pong.ycor())
    user_plank.goto(-350, pong.ycor())

    if pong.ycor() > 279.99 or pong.ycor() < -279.99:
        prev_angle_y = pong.heading()

    if pong.ycor() > 280:
        if prev_angle_y < 90:
            pong.bounce_downright()
        else:
            pong.bounce_downleft()

    if pong.ycor() < -280:
        if 180 < prev_angle_y < 270:
            pong.bounce_upleft()
        else:
            pong.bounce_upright()

    if pong.xcor() > 410:
        pong.goto(0, 0)
        pong.angle += 180
        user_score.add_score()
        pong.pace = 0

    if pong.xcor() < -410:
        pong.goto(0, 0)
        pong.angle += 180
        cpu_score.add_score()
        pong.pace = 0

    if user_plank.distance(pong.pos()) < 50:
        if pong.xcor() < -330:
            print("made contact")
            diff_user = pong.distance(user_plank.pos())

            if pong.ycor() > user_plank.ycor():

                pong.angle = diff_user
                prev_angle_y = pong.angle
                pong.pace += 0.15

                print(f"prev angle: {prev_angle_y}")

            else:

                pong.angle = (-1 * diff_user)
                prev_angle_y = pong.angle
                pong.pace += 0.15
                print(f"prev angle: {prev_angle_y}")

    if cpu_plank.distance(pong.pos()) < 50:
        if pong.xcor() > 330:
            print("made contact")
            diff_user = pong.distance(cpu_plank.pos())

            if pong.ycor() > cpu_plank.ycor():

                pong.angle = (180 - diff_cpu) - 15
                prev_angle_y = pong.angle
                pong.pace += 0.15
                print(f"prev angle: {prev_angle_y}")
            else:
                pong.angle = (180 + diff_cpu) + 15
                prev_angle_y = pong.angle
                pong.pace += 0.15
                print(f"prev angle: {prev_angle_y}")
screen.exitonclick()
