from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("black", "orange")
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-290, 290)
        rand_y = random.randint(-290, 290)
        self.goto(rand_x, rand_y)
