def course():
    a = input("enter your course code: ")
    if len(a) == 6:
        if a[:3].isupper():
            if a[3:].isdigit():
                print("accepted")
                return True
            else:
                return False
        else:
            return False
    else:
        return False
#course()

def color():
    b = input("enter your color in hexadecimal format: #")
    c = 0
    if len(b) == 6:
        for i in b:
            if i.isdigit() or i.isalpha():
                c += 1
            else:
                print("invalid")
    else:
        print("invalid")
    if c == 6:
        print("valid")
#color()

import re
def number():
    d = input("enter a paragraph: ")
    e = re.findall('[0-9]+',d)
    print(e)
    f = 0
    for i in e:
        f = f +int(i)
    print(f)
#number()

import re
def phone_number():
    a = input("enter your phone number ")
    print(re.sub(r'[0-9]{10}|/+84[0-9]+', '[REDACTED]',a))
#phone_number()