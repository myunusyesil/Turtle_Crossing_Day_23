import time
from threading import Thread
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(fun=player.move, key='Up')

cars = []


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Generate random cars along y-axis and move it
    new_car = CarManager()
    cars.append(new_car)
    for car in cars:
        car.move()


screen.exitonclick()

