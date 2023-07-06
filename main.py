import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
screen.listen()
screen.onkeypress(fun=player.move, key='Up')

cars = []
first_car = CarManager()
cars.append(first_car)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Generate random cars along y-axis and move it
    # Reduce the car generation with random and for function
    num = random.randint(0, 10)
    if num > 8:
        new_car = CarManager()
        if cars[-1].distance(new_car) > 60:
            cars.append(new_car)
    for car in cars:
        car.move(score.level)

    # Detect if turtle hits the top edge of the screen
    if player.ycor() > 280:
        player.reach_finish()
        print(score.level)
        score.update_scoreboard()

    # Detect if the turtle hits the cars?
    for rolling_cars in cars:
        if player.distance(rolling_cars) < 25:
            print("Crash happened!")
            game_is_on = False
            score.game_over()




screen.exitonclick()

