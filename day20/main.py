from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
# https://docs.python.org/3.3/library/time.html

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("light pink")
screen.title("Snake game!!!")
screen.tracer(0)   # deactivate tracer


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.4)  # more lower, move faster

    snake.move()


    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    # if head collid with any segment in the tail:
    #     trigger game_over


# new line in if
# https://stackoverflow.com/questions/181530/styling-multi-line-conditions-in-if-statements





screen.exitonclick()
# screen.mainloop()