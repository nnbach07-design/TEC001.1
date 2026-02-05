def invisible3():
    a = 1
    while a <= 1000:
        if a % 3 == 0:
            print(a)
        a += 1
invisible3()

def inch_to_cm():
    while True:
        inch = float(input("inches: "))
        if inch < 0:
            break
        print(inch * 2.54)
inch_to_cm()

def min_max_numbers():
    numbers = []

    while True:
        b = input("number: ")
        if b == "":
            break
        numbers.append(float(b))

    print("smallest:", min(numbers))
    print("largest:", max(numbers))
min_max_numbers()

def guess_game():
    import random
    number = random.randint(1, 10)

    while True:
        guess = int(input("guess a number (1-10): "))
        if guess < number:
            print("too low")
        elif guess > number:
            print("too high")
        else:
            print("correct")
            break
guess_game()

def login():
    count = 0

    while count < 5:
        username = input("username: ")
        password = input("password: ")

        if username == "python" and password == "rules":
            print("Welcome")
            return

        print("Wrong credentials")
        count += 1

    print("Access denied")
login()

def middle_char():
    c = input("enter a string: ")
    d = len(c)

    if d % 2 == 0:
        print(c[d//2 - 1 : d//2 + 1])
    else:
        print(c[d//2])
middle_char()

def acronym():
    phrase = input("enter a phrase: ")
    words = phrase.split()
    result = ""

    for w in words:
        result += w[0].upper()

    print(result)
acronym()
