import turtle
from turtle import Turtle, Screen
from snake import Snake
import time
from snake_food import Food
from scoreboard import Scoreboard




# this explain how screen should behave
my_screen = Screen()
my_screen.setup(width= 500, height = 500)
my_screen.bgcolor("black")
# my_screen.title("snake game")
# my_screen.tracer(0)

# this explain key control
snake = Snake()
my_screen.listen()
my_screen.onkey(snake.moveup, "Up")
my_screen.onkey(snake.movedown, "Down")
my_screen.onkey(snake.moveleft,"Left")
my_screen.onkey(snake.moveright,"Right")

turtle.tracer(0)
score = 0


snake.create_snake()
snake_food = Food()
scoreboard = Scoreboard()


is_game_on = True
while is_game_on:
    # this part was pretty tricky for me
    # i recomend you to go through these line again & again
    my_screen.update()
    time.sleep(0.15)
    snake.move()

    # if detected collision with food(using distance method of turtle)
    if snake.head.distance(snake_food) <20:
        snake_food.random_location()
        scoreboard.update_score()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 245 or snake.head.xcor() < -245 or snake.head.ycor()>240 or snake.head.ycor()<-240:
        is_game_on = False
        scoreboard.game_over()

    # if snake eat itself
    for segement in snake.segement[1:]:
        if snake.head.distance(segement)<10:
            is_game_on = False
            scoreboard.game_over()
        # if segement == snake.head:
        #     pass
        # elif snake.head.distance(segement)< 10:
        #     is_game_on = False
        #     scoreboard.game_over()



my_screen.exitonclick()
