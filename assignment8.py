class elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom
    def floor_up(self):
        self.current += 1
        print("Moved up one floor")
        print("Current floor:", self.current)
    def floor_down(self):
        self.current -= 1
        print("Moved down one floor")
        print("Current floor:", self.current)
    def go_to_floor(self, floor):
        print("Current floor:", self.current)
        while floor != self.current:
            if floor > self.current:
                if self.current < self.top:
                    self.floor_up()
                else:
                    print("You reached the top floor")
                    break
            else:
                if self.current > self.bottom:
                    self.floor_down()
                else:
                    print("You reached the bottom floor")
                    break
#a = elevator(-10, 10)
#a.go_to_floor(-11)

class building:
    def __init__(self, top, bottom, elevators):
        self.top = top
        self.bottom = bottom
        self.elevators = []
        for i in range(elevators):
            e = elevator(self.bottom, self.top)
            self.elevators.append(e)
    def run_elevator(self, elenum, destination):
        print("")
        print("This is elevator number", elenum)
        ele = self.elevators[elenum - 1]
        ele.go_to_floor(destination)

    def fire_alarm(self):
        print()
        for e in self.elevators:
            e.go_to_floor(self.bottom)
        print("All the elevators are moved to the bottom floor due to fire alarm.")
#b = building(10, -10, 3)
#b.run_elevator(1, 3)
#b.run_elevator(2, 2)
#b.run_elevator(3, 20)
#b.fire_alarm()

#4
#from assignment 7
#1
class car:
    def __init__(self, rn, ms):
        self.rn = rn
        self.ms = ms
        self.cs = 0
        self.td = 0
#2
    def accelerate(self, speed):
        self.cs = self.cs + speed
        if self.cs > self.ms:
            self.cs = self.ms
        elif self.cs < 0:
            self.cs = 0
#3
    def drive(self, hours):
        distance = self.cs * hours
        self.td += distance
#continue assignment 8
import random
class race:
    def __init__(self, name, distance, participation):
        self.name = name
        self.distance = distance
        self.participation = participation
    def hour_passes(self):
        for c in self.participation:
            c.accelerate(random.randint(-10, 15))
            c.drive(1)
    def print_status(self):
        for c in self.participation:
            print(f"Registration number: {c.rn}, Maximum speed: {c.ms}, Current speed: {c.cs}, Tavelled distance: {c.td}")
    def race_finished(self):
        for c in self.participation:
            if c.td >= self.distance:
                return True
        return False
cars = []
for i in range(1, 11):
    c = car(f"ABC-{i}", random.randint(150, 200))
    cars.append(c)
r = race("Grand Demolition Derby", 8000, cars)
h = 0
while not r.race_finished():
    h += 1
    r.hour_passes()
    if h % 10 == 0:
        r.print_status()
print("Final results:")
r.print_status()