class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed):
        self.current_speed = self.current_speed + speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        distance = self.current_speed * hours
        self.travelled_distance += distance

import random
cars = []
for i in range(1,11):
    car = Car(f"ABC-{i}", random.randint(150, 200))
    cars.append(car)
a = True
while a == True:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.travelled_distance >= 10000:
            c = False
cars.sort(key=lambda d: d.td, reverse=True)
for car in cars:
    print(f"Registration number: {car.registration_number}, Maximum speed: {car.maximum_speed}, Final current speed: {car.current_speed}, Final travelled distance: {car.travelled_distance}")