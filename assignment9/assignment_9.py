#1
def lines(path):
    with open(path, encoding="utf-8") as a:
        b = 0
        for line in a:
            if line.strip():
                b += 1
    print(b)
#lines("test.txt")

#2
def keywords(path, keyword):
    a = []
    with open(path, encoding="utf-8") as b:
        c = 1
        for line in b:
            if keyword in line:
                a.append("Line " + str(c))
            c += 1
    print(a)
#keywords("test.txt", "the")

#3
def uppercase(path):
    with open(path, "r") as a:
        b = a.read()
    c = b.upper()
    with open("output.txt", "w") as d:
        d.write(c)
#uppercase("input.txt")

#4
def average(path):
    a = 0
    b = 0
    with open(path) as c:
        for line in c:
            d, e = line.strip().split(",")
            a += int(e)
            b += 1
    return a / b
print(average("test.txt"))