#1
import requests
import json
def joke():
    a = "https://api.chucknorris.io/jokes/random"
    b = requests.get(a).json()
    #print(json.dumps(b))
    print("The random Chuck Norris joke:", b["value"])
#joke()

#2
def openweather():
    a = input("Enter the name of a municipality: ")
    b = f"http://api.openweathermap.org/geo/1.0/direct?q={a}&limit=5&appid=8c38eb05781e6ee8ca27fc247abc054a"
    c = requests.get(b).json()
    #print(json.dumps(c))
    d = f"https://api.openweathermap.org/data/2.5/weather?lat={c[0]["lat"]}&lon={c[0]["lon"]}&appid=8c38eb05781e6ee8ca27fc247abc054a"
    e = requests.get(d).json()
    #print(json.dumps(e))
    # f = e["weather"]["description"]
    # g = e["main"]["temp"] - 273.15
    print("Weather description:", e["weather"][0]["description"])
    print("Temperature:", e["main"]["temp"] - 273.15, "degree C")
#openweather()

#3
from flask import Flask
def isprime():

    a = Flask(__name__)
    @a.route("/prime_number/<n>")
    def prime(n):
        n = int(n)
        b = True
        if n < 2:
            b = False
        for i in range(2, n):
            if n % i == 0:
                b = False
        return {
            "Number": n,
            "isPrime": b
        }
    if __name__ == '__main__':
        a.run(host='127.0.0.1', port=5000)
#isprime()

#4
import json
with open(r"D:\VSCode\python\uni\hw\airports.json", "r", encoding="utf-8") as a:
    b = json.load(a)
def icao():
    c = Flask(__name__)
    @c.route("/airport/<d>")
    def airport(d):
        d = d.upper()
        if d in b:
            e = b[icao]
            output = {

            }
    if __name__ == '__main__':
        c.run(host='127.0.0.1', port=5000)