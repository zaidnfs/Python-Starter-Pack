import time
import snake
import turtle
import food
import scoreboard

screen = turtle.Screen()
screen.title("My snake game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = snake.Snake()
food = food.Food()
score = scoreboard.Scoreboard()
screen.listen()

screen.onkey(snake.up,key="w")
screen.onkey(snake.down,key="s")
screen.onkey(snake.right,key="d")
screen.onkey(snake.left,key="a")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #Collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake.reset_snake()
        score.reset_score()
        food.refresh()
        # game_is_on = False
        # score.game_over()

    #Collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10 :
            snake.reset_snake()
            score.reset_score()
            # game_is_on = False
            # score.game_over()

screen.exitonclick()