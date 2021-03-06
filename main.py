# Snake Game
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Game Proper
game_running = True
while game_running:

    screen.listen()
    screen.onkey(key="Up", fun=snake.go_up)
    screen.onkey(key="Down", fun=snake.go_down)
    screen.onkey(key="Left", fun=snake.go_left)
    screen.onkey(key="Right", fun=snake.go_right)

    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.reappear()
        scoreboard.snake_scores()
        scoreboard.keep_score()
        snake.grow()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        scoreboard.is_high_score()
        if scoreboard.play_again():
            snake.reset_snake()
            scoreboard.keep_score()
        else:
            game_running = False

    # Detect collision with self
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 15:
            scoreboard.game_over()
            scoreboard.is_high_score()
            if scoreboard.play_again():
                snake.reset_snake()
                scoreboard.keep_score()
            else:
                game_running = False


screen.exitonclick()
