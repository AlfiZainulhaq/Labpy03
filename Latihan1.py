from random import random

# Meminta input dari user
n = int(input("Masukkan nilai N: "))

i = 0
count = 0

# Gunakan while untuk mengulang hingga jumlah data = n
while count < n:
    a = random()
    # hanya tampilkan bila a < 0.5
    if a < 0.5:
        count += 1
        print(f"data ke: {count} => {a}")
print("Selesai")

print("selesai")