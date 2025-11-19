import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

#Screen setup
scoreboard = Scoreboard()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

#Paddle setup

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Collision with paddles
    if ball.distance(right_paddle) < 60 and ball.xcor() > 320 or ball.distance(left_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    #Right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()