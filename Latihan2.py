modal = 100000000  # modal awal
laba_total = 0     # untuk menyimpan total laba

for bulan in range(1, 9):  # dari bulan 1 sampai 8
    if bulan in [1, 2]:
        laba = 0
    elif bulan in [3, 4]:
        laba = modal * 0.01
    elif bulan in [5, 6, 7]:
        laba = modal * 0.05
    else:  # bulan ke-8
        laba = modal * 0.03

    laba_total += laba
    print(f"laba bulan ke-{bulan} sebesar: {laba}")

print(f"Total laba adalah: {laba_total}")
