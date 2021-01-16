from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Cars(Turtle):

    def __init__(self, list_of_cars):
        super().__init__()
        self.all_cars = []
        self.cars = list_of_cars
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            car_index = random.choice(self.cars)
            new_car.shape(car_index)
            random_y = random.randrange(-230, 230, 60)
            new_car.penup()
            random_x = random.randrange(280, 400, 75)
            new_car.goto(random_x, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

