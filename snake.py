# Create the snake
from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body = []
        self.birth_snake()
        self.head = self.body[0]

    def birth_snake(self):
        x_start = 0
        for _ in range(3):
            turtle = Turtle(shape="square")
            turtle.color("white")
            turtle.penup()
            turtle.setx(x_start)
            x_start -= 20
            self.body.append(turtle)

    def move(self):
        for segment in range(len(self.body) - 1, 0, -1):
            position_x = self.body[segment - 1].xcor()
            position_y = self.body[segment - 1].ycor()
            self.body[segment].goto((position_x, position_y))
        self.head.forward(MOVE_DISTANCE)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        turtle = Turtle(shape="square")
        # turtle.position_x = self.body[-1].xcor()
        # turtle.position_y = self.body[-1].ycor()
        # This turned out to be just another way of doing the same thing (with or without hiding the turtle).
        turtle.hideturtle()
        turtle.color("white")
        turtle.penup()
        self.body.append(turtle)
        turtle.showturtle()
