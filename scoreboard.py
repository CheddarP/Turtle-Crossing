from turtle import Turtle

LEVEL_FONT = ("Courier", 30, "normal")
GAME_OVER_FONT = ("Courier", 70, "normal")
ALIGN_LEFT = "left"
ALIGN_CETNER = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 0
        self.hideturtle()
        self.color("maroon")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.goto(-280, 270)
        self.write(f"Level: {self.level}", move=False, align=ALIGN_LEFT, font=LEVEL_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGN_CETNER, font=LEVEL_FONT)
