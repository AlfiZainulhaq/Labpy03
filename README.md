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

