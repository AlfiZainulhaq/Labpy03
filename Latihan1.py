from random import random

# input dari user
n = int(input("Masukkan nilai N: "))

i = 0
while i < n:
    a = random()
    if a < 0.5:
        print(f"data ke: {i+1} => {a}")
        i += 1

print("Selesai")