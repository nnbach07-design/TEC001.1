def greet():
    a = input("what your name: ")
    print("hello", a)
greet()

import math
def circumference():
    radius = float(input("radius: "))
    print("circumference", math.pi * radius * 2)
circumference()

def rectangle():
    length = int(input("length:"))
    width = int(input("width:"))
    print("perimeter", 2 * length + 2 * width)
    print("are" , length * width)
rectangle()

def integer():
    number1 = int(input("first number:"))
    number2 = int(input("second number:"))
    number3 = int(input("third number:"))
    print("sum", number1 + number2 +number3)
    print("product", number1 * number2 *number3)
    print("average", (number1 + number2 + number3)/3)
integer()

def medieval():
    talent = 8512 * float(input("talent:"))
    pound = 425.6 * float(input("pound:"))
    lot = 13.3 * float(input("lot:"))
    total = talent + pound + lot
    if total >1000:
        kg = int(total / 1000)
        g = total - kg * 1000
    else:
        kg = 0
        g = total
    print("The weight in modern units:", kg, "and", g)
medieval()

import random
three_digit = ""
for i in range(3):
    three_digit += str(random.randint(0, 9))
four_digit = ""
for i in range(4):
    four_digit += str(random.randint(1, 6))

print("three-digit combination (0-9):", three_digit)
print("four-digit combination (1-6):", four_digit)
