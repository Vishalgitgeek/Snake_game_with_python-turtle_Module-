from turtle import Turtle
import random

class Food(Turtle):



    def __init__(self):
        # self.random_location()
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.shapesize(stretch_len=0.4,stretch_wid=0.4)

    def random_location(self):
        x_coor = random.randint(-200, 200)
        y_coor = random.randint(-200, 200)

        self.goto(x_coor, y_coor)

