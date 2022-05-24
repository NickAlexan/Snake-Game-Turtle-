from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Snake's Snail Snacks")
screen.tracer(0)


snake = Snake()
food = Food()
scrbrd = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    if snake.head.distance(food) < 15:
        scrbrd.score_up()
        food.refresh()
        snake.grow()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scrbrd.game_over()

    for part in snake.snake[1:]:
        if snake.head.distance(part) < 10:
            game_is_on = False
            scrbrd.game_over()

screen.exitonclick()
