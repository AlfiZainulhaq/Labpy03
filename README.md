# Labpy03

## Latihan 1 <a href="Latihan1.py">file</a>

<pre>from random import random </pre>

Mengimpor fungsi random() dari modul random bawaan Python yang menghasilkan angka acak dari 0.0 sampai 1.0.

<pre>n = int(input("Masukkan nilai N: "))</pre>

Program meminta user memasukkan jumlah n atau data yang ingin ditampilkan.

<pre>i = 0</pre>

melacak berapa angka yang sudah dicetak.

<pre>while i < n:</pre>

Loop akan terus berjalan selama jumlah angka yang ditampilkan belum sama dengan n, jika sudah loop akan berhenti.

<pre>a = random()</pre>

Setiap perulangan, program membuat angka acak baru antara 0 dan 1.

<pre>if a < 0.5:</pre>

jika a lebih dari 0.5 program tidak akan mencetak dan mencari angka baru lagi. program hanya mencetak angka kurang dari 0.5

<pre>print(f"data ke: {i+1} => {a}")</pre>

Menampilkan nomor data dan nilainya dengan format rapi.

<pre>i += 1</pre>

Menambah hitungan data setiap kali ada angka yang dicetak.

## Latihan 2 <a href="Latihan2.py">file</a>

<pre>modal = 100_000_000
total_laba = 0</pre>

modal adalah uang awal 100 juta.<br>
total_laba diset 0 dulu karena belum ada laba di awal.

<pre>for bulan in range(1, 9):</pre>

range(1, 9) menghasilkan angka perulangan 1,2,3,4,5,6,7,8.

<pre>if bulan <= 2:
        persen = 0</pre>

Untuk bulan 1 dan 2, tidak ada laba (0%).

<pre>elif bulan <= 4:
        persen = 1</pre>

Untuk bulan 3 dan 4, laba naik jadi 1% dari modal.

<pre>elif bulan <= 7:
        persen = 5</pre>

Untuk bulan 5, 6, dan 7, laba meningkat jadi 5%.

<pre> else:
        persen = 2</pre>

Untuk bulan ke 8, laba turun menjadi 2%.

<pre>laba = modal * (persen / 100)</pre>

Menghitung laba bulan itu berdasarkan persen.

<pre>print(f"laba bulan ke-{bulan} sebesar: {laba}")</pre>

Menampilkan hasil laba tiap bulan di layar.

<pre>total_laba += laba</pre>

Menambahkan laba bulan ini ke total semua laba.

<pre>print(f"Total laba adalah: {total_laba}")</pre>

menampilkan hasil akhir total laba dari bulan 1–8.
