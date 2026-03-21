def greatest_number():
    numbers = []

    while True:
        a = input("enter numbers: ")
        if a == "":
            break
        numbers.append(int(a))

    numbers.sort(reverse=True)

    print("5 greatest numbers: ")
    print(numbers[:5])
#greatest_number()

def prime_number():
    a = int(input("enter a number: "))
    if a < 2:
        print(a,"is not a prime number")
    else:
        for i in range(2, a):
            if a % i == 0:
                print(a, "is not a prime number")
                break
        else:
            print(a,"prime number")
#prime_number()

def cities():
    cities = []
    for i in range(5):
        a = input("enter 5 city: ")
        cities.append(a)
    for city in cities:
        print(city)
#cities()

def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
input_numbers = input("enter a list of number: ")
numbers = []
for i in input_numbers.split():
    numbers.append(int(i))
total = sum_numbers(numbers)
print("the sum of the number is:", total)
#sum_numbers(numbers)

def odd():
    a = input("Enter list of numbers: ")
    b = []
    for i in a.split(","):
        b.append(int(i))
    c = []
    for o in b:
        if o % 2 == 0:
            c.append(o)
    print("The original:", b)
    print("The cut-down:", c)
#odd()