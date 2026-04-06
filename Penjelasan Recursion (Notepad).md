###### **1. Fungsi sum\_of\_digits(n)**

###### 

Fungsi rekursif untuk menjumlahkan setiap angka dalam sebuah bilangan bulat.



* def sum\_of\_digits(n): membuat fungsi yang menerima satu parameter bilangan bulat.
* if n == 0: kondisi berhenti ketika bilangan sudah habis (tidak ada digit lagi).
* return 0 mengembalikan 0 sebagai identitas penjumlahan.
* return n % 10 + sum\_of\_digits(n // 10) mengambil digit terakhir (sisa bagi 10), lalu memanggil diri sendiri dengan bilangan yang sudah dibuang digit terakhirnya (pembagian bulat 10).
* print("Sum of digits:", sum\_of\_digits(112)) menjalankan fungsi dengan input 112, hasilnya 1+1+2 = 4.

Kompleksitas: O(d) — d adalah jumlah digit dalam bilangan n.







###### **2. Fungsi power(x, n)**



Fungsi rekursif untuk menghitung nilai x pangkat n (versi sederhana).

* def power(x, n): mendeklarasikan fungsi dengan dua parameter: basis dan eksponen.
* if n == 0: kondisi dasar perhitungan pangkat.
* return 1 semua bilangan pangkat 0 bernilai 1.
* return x \* power(x, n - 1) mengalikan basis dengan hasil pangkat yang lebih kecil satu.
* print("Power:", power(2, 4)) menjalankan fungsi dengan 2 pangkat 4, hasilnya 16.

Kompleksitas: O(n) — linear terhadap nilai eksponen n.







###### **3. Fungsi gcd(a, b)**



Fungsi rekursif untuk mencari Faktor Persekutuan Terbesar (Greatest Common Divisor) menggunakan algoritma Euclid.



* def gcd(a, b): membuat fungsi dengan dua parameter bilangan bulat.
* if b == 0: kondisi berhenti ketika pembagi sudah nol.
* return a mengembalikan a sebagai FPB terakhir.
* return gcd(b, a % b) memanggil diri sendiri dengan menukar posisi: b menjadi a, sisa bagi a dengan b menjadi b baru.
* print("GCD:", gcd(48, 18)) menjalankan fungsi dengan 48 dan 18, hasilnya 6.

Kompleksitas: O(log min(a,b)) — sangat efisien karena nilai berkurang drastis tiap iterasi.







###### **4. Fungsi decimal\_to\_binary(n)**



Fungsi rekursif untuk mengkonversi bilangan desimal menjadi representasi biner dalam bentuk angka desimal (bukan string).



* def decimal\_to\_binary(n): mendeklarasikan fungsi konversi.
* if n == 0: kondisi berhenti ketika bilangan sudah habis.
* return 0 dasar rekursi.
* return n % 2 + 10 \* decimal\_to\_binary(n // 2) mengambil bit terakhir (0 atau 1), lalu menempatkannya di posisi satuan dengan menggeser hasil rekursi ke kiri (dikalikan 10).
* print("Binary:", decimal\_to\_binary(10)) menjalankan fungsi dengan input 10, hasilnya 1010 (yang dibaca sebagai seribu sepuluh dalam desimal, tapi merepresentasikan 1-0-1-0 dalam biner).

Kompleksitas: O(log n) — bergantung pada jumlah bit yang dibutuhkan.

