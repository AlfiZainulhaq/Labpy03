from random import random

n = int(input("Masukkan nilai N: "))

i = 0
count = 0

while count < n:
    a = random()
    if a < 0.5:
        count += 1
        print(f"data ke: {count} => {a}")
print("Selesai")
