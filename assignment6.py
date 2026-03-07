def greatest_number():
    numbers = []
    while True:
        a = input("enter a number: ")
        if a == "":
            break
        numbers.append(int(a))
    numbers.sort(reverse=True)
    print("five greatest numbers: ", numbers[:5])
#greatest_number()

def seasons():
    a = ("Winter", "Spring", "Summer", "Autumn")
    b = int(input("enter the month number: "))
    c = (b % 12) // 3
    print("It is:", a[c])
#seasons()

def names():
    a = set()
    while True:
        name = input("enter a name: ")
        if name == "":
            break
        elif name in a:
            print("existing Name")
        else:
            print("new Name")
            a.add(name)
    print("names entered:", a)
#names()

def word_frequency(text):
    a = {}
    b = text.split()
    for i in b:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    return a


text = input("enter text: ")
print(word_frequency(text))
#word_frequency(text)

def remove_numbers(odds):
    a = []
    for number in odds:
        if number % 2 == 0:
            a.append(number)
    return a

b =(input("enter a list of numbers: "))
c = []
for i in b.split():
    c.append(int(i))
d = remove_numbers(c)

print("original list: ", c)
print("new list: ", d)

