import time
from turtle import Screen
from player import Player
from car_manager import Cars
from scoreboard import Scoreboard

cars = ["car1.gif", "car2.gif", "car4.gif", "car5.gif", "car6.gif", "car7.gif", "car8.gif"]

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.bgpic("highway1.gif")
for car_index in cars:
    screen.register_shape(car_index)
screen.tracer(0)

player = Player()
car_manager = Cars(cars)
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")
screen.onkey(fun=player.move_down, key="Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move()

    #collision with the car:

    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            game_on = False
            scoreboard.game_over()

    #successful crossing:
    if player.is_at_finish_line():
        player.starting_position()
        car_manager.level_up()
        scoreboard.update_scoreboard()



screen.exitonclick()
