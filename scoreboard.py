from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Level: {self.level}', align='left', font=FONT, move=False)
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over', align='center', font=FONT, move=False)
