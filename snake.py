from turtle import Turtle
from random import random
STARTING_COORDINATE = [(0, 0)]


class Snake:
    def __init__(self):

        # this will contain the body parts of snake
        self.segement = []
        self.create_snake()
        self.head = self.segement[0]
        


    def create_snake(self):
        for coordinate in STARTING_COORDINATE:
            self.add_segment(coordinate)

    def add_segment(self,coordinate):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(coordinate)
        self.segement.append(new_turtle)
    

    def extend(self):
        self.add_segment(self.segement[-1].position())

    def move(self):
        for turtle_num in range((len(self.segement) - 1), 0, -1):
            new_xcoor = self.segement[turtle_num-1].xcor()
            new_ycoor = self.segement[turtle_num-1].ycor()
            self.segement[turtle_num].goto(new_xcoor, new_ycoor)
        self.segement[0].forward(20)

    def moveup(self):
        self.head.setheading(90)

    def movedown(self):
        self.head.setheading(270)

    def moveleft(self):
        self.head.setheading(180)

    def moveright(self):
        self.head.setheading(0)






