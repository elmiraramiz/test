import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake #snake=file name , Snake= class name

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()   #snake=object
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)
    if snake.segments[0].distance(food) < 20:
        food.refresh()
        scoreboard.add()
screen.exitonclick()
