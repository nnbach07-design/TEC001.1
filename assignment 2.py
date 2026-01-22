def zander():
    a = float(input("length of a zander in centimeters:"))
    if a < 42:
        print("please release the fish back into the lake because your fish is shorter than the size limit",42 - a,"cm")
        print("a zander must be 42 centimeters or longer to meet the size limit")
    else:
        print("your zander is good")
zander()

def cabin_class():
    a = input("enter your cabin class:")
    if a == "LUX":
        print("LUX: upper-deck cabin with a balcony.")
    elif a == "A":
        print("A: above the car deck, equipped with a window.")
    elif a == "B":
        print("B: windowless cabin above the car deck.")
    elif a == "C":
        print("C: windowless cabin below the car deck.")
    else:
        print("Invalid cabin class!")
cabin_class()

def hemoglobin_value():
    a = input("your biological sex:")
    b = int(input("your hemoglobin value:"))
    if a == "female":
        if b < 117:
            print("your hemoglobin value is low")
        elif b <=155:
            print("your hemoglobin value is normal")
        else:
            print("your hemoglobin value is high")
    elif a == "male":
        if b < 134:
            print("your hemoglobin value is low")
        elif b <=167:
            print("your hemoglobin value is normal")
        else:
            print("your hemoglobin value is high")
hemoglobin_value()

def leap_year():
    a = int(input("enter a year:"))
    if a % 100 == 0:
        if a % 400 == 0:
            print("that is a leap year")
        else:
            print("that is not a leap year")
    elif a % 4 == 0:
        print("that is a leap year")
    else:
        print("that is not a leap year")
leap_year()

import math

def cal(x):
    a = float(input(f"Enter the diameter of the {x} round pizza(cm): "))
    b = float(input(f"Enter the price of the {x} pizza(USD): "))
    c = b / (((a / 100) / 2) ** 2 * math.pi)
    return c

def com():
    a = cal("first")
    b = cal("second")
    if a < b:
        print("The first pizza provides better value for money")
    else:
        print("The second pizza provides better value for money")

com()