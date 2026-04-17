import requests
a = "http://127.0.0.1:5000//prime_number/31"
b = requests.get(a).json()
print(b)