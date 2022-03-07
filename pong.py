from turtle import Turtle
from UserPlank import UserPlank
import random


class Pong(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.signx = 10
        self.signy = 10
        self.angle = random.randint(0,360)
        self.diff = 0
        self.pace = 0

    def initial_motion(self):
        self.setheading(self.angle)
        self.forward(3 + self.pace)


    def bounce_upright(self):
        self.angle = 45

    def bounce_upleft(self):
        self.angle = 135

    def bounce_downleft(self):
        self.angle = 225

    def bounce_downright(self):
        self.angle = 315






        



