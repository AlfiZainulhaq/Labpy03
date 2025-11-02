modal = 100_000_000
total_laba = 0

for bulan in range(1, 9):
    if bulan <= 2:
        persen = 0
    elif bulan <= 4:
        persen = 1
    elif bulan <= 7:
        persen = 5
    else:
        persen = 2
    
    laba = modal * (persen / 100)
    print(f"laba bulan ke-{bulan} sebesar: {laba}")
    total_laba += laba

print(f"Total laba adalah: {total_laba}")
