from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.speed(1)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(COLORS))
        pos_y = (random.randint(-28, 28))*20
        self.goto(320, pos_y)

    def move(self):
        self.setheading(180)
        self.forward(STARTING_MOVE_DISTANCE)
