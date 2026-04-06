* ###### **1. Fungsi foo(array)**



Fungsi ini menghitung jumlah (sum) dan hasil kali (product) elemen dalam array.



* def foo(array): mendefinisikan fungsi dengan parameter array.
* sum = 0 inisialisasi variabel sum ke 0.
* product = 1 inisialisasi variabel product ke 1.
* for i in array: loop pertama untuk menjumlahkan semua elemen.
* sum += i menambahkan elemen ke variabel sum.
* for i in array: loop kedua untuk mengalikan semua elemen.
* product \*= i mengalikan elemen ke variabel product.
* print("Sum = "+str(sum)+", Product = "+str(product)) mencetak hasil akhir.
* ar1 = \[1,2,3,4] membuat array dengan nilai \[1,2,3,4].
* foo(ar1) memanggil fungsi (output: Sum = 10, Product = 24).

**Kompleksitas:** O(n) — dua loop linear terpisah, n = panjang array.







###### **2. Fungsi printPairs(array)**



Fungsi ini mencetak semua pasangan elemen (termasuk duplikasi dan pasangan sama).



* def printPairs(array): mendefinisikan fungsi dengan parameter array.
* for i in array: loop luar iterasi setiap elemen.
* for j in array: loop dalam iterasi setiap elemen lagi (nested).
* print(str(i)+","+str(j)) mencetak pasangan (i,j).
* printPairs(\[1,2,3]) memanggil fungsi dengan array \[1,2,3].

Output: semua 9 pasangan ("1,1", "1,2", "1,3", "2,1", "2,2", "2,3", "3,1", "3,2", "3,3").

**Kompleksitas:** O(n²) — nested loop, quadratic time.







###### **3. Fungsi printUnorderedPairs(array)**



Fungsi ini mencetak pasangan unik tanpa duplikasi (hanya i < j).



* def printUnorderedPairs(array): mendefinisikan fungsi dengan parameter array.
* for i in range(0,len(array)): loop luar dengan indeks dari 0 sampai n-1.
* for j in range(i+1,len(array)): loop dalam dari i+1 sampai akhir.
* print(str(array\[i]) + "," + str(array\[j])) mencetak pasangan unik.
* array = \[1,2,3,4,5] membuat array dengan 5 elemen.
* printUnorderedPairs(array) memanggil fungsi.

Output: 10 pasangan unik ("1,2", "1,3", "1,4", "1,5", "2,3", "2,4", "2,5", "3,4", "3,5", "4,5").

**Kompleksitas:** O(n²) — nested loop dengan setengah iterasi, tetap quadratic.







###### **4. Fungsi printUnorderedPairs(arrayA, arrayB)**



Fungsi ini mencetak pasangan dimana elemen A lebih kecil dari elemen B.



* def printUnorderedPairs(arrayA, arrayB): mendefinisikan fungsi dengan dua parameter array.
* for i in range(len(arrayA)): loop luar iterasi arrayA.
* for j in range(len(arrayB)): loop dalam iterasi arrayB.
* if arrayA\[i] < arrayB\[j]: kondisi filter hanya jika A < B.
* print(str(arrayA\[i]) + "," + str(arrayB\[j])) mencetak pasangan yang memenuhi kondisi.
* arrayA = \[1,2,3,4,5] dan arrayB = \[2,6,7,8] definisi dua array.
* printUnorderedPairs(arrayA, arrayB) memanggil fungsi.

**Kompleksitas:** O(a × b) — a = panjang arrayA, b = panjang arrayB.







###### **5. Fungsi printUnorderedPairs dengan loop konstan**



Fungsi ini sama seperti nomor 4 tapi dengan loop sia-sia (wasteful) sebanyak 100.000 kali.



* def printUnorderedPairs(arrayA, arrayB): definisi sama dengan nomor 4.
* for i in range(len(arrayA)): loop luar iterasi arrayA.
* for j in range(len(arrayB)): loop dalam iterasi arrayB.
* for k in range(0,100000): loop ketiga konstan 100.000 iterasi.
* print(str(arrayA\[i]) + "," + str(arrayB\[j])) mencetak pasangan.
* arrayA = \[1,2,3,4,5] dan arrayB = \[2,6,7,8] definisi array.
* printUnorderedPairs(arrayA,arrayB) memanggil fungsi.

**Kompleksitas:** O(a × b) — konstanta 100.000 diabaikan dalam Big O notation.







###### **6. Fungsi reverse(array)**



Fungsi ini membalik array secara in-place dengan menukar elemen dari luar ke dalam.



* def reverse(array): mendefinisikan fungsi dengan parameter array.
* for i in range(0,int(len(array)/2)): loop setengah panjang array.
* other = len(array)-i-1 menghitung indeks pasangan dari belakang.
* temp = array\[i] menyimpan elemen sementara.
* array\[i] = array\[other] menukar elemen depan dengan belakang.
* array\[other] = temp menukar elemen belakang dengan depan.
* print(array) mencetak array yang sudah terbalik.
* arrayA = \[1,2,3,4,5] membuat array.
* reverse(arrayA) memanggil fungsi (output: \[5,4,3,2,1]).

**Kompleksitas:** O(n) — loop n/2 kali, linear time.







###### **8. Fungsi factorial(n)**



Fungsi ini menghitung faktorial menggunakan rekursi.



* def factorial(n): mendefinisikan fungsi dengan parameter n.
* if n < 0: validasi input negatif.
* return -1 mengembalikan -1 untuk input invalid.
* elif n == 0: base case faktorial 0.
* return 1 faktorial 0 = 1.
* else: recursive case untuk n positif.
* return n \* factorial(n-1) rumus rekursif n! = n × (n-1)!.
* print(factorial(3)) memanggil fungsi (output: 6, karena 3×2×1=6).

**Kompleksitas:** O(n) — n panggilan rekursif, linear time.







###### **9. Fungsi allFib(n) dan fib(n)**



Fungsi ini mencetak deret Fibonacci dari 0 sampai n-1 menggunakan rekursi naif.



* def allFib(n): fungsi utama untuk mencetak semua Fibonacci.
* for i in range(n): loop dari 0 sampai n-1.
* print(str(i)+":, " + str(fib(i))) mencetak indeks dan nilai fib(i).
* def fib(n): fungsi rekursif Fibonacci.
* if n <= 0: base case untuk 0.
* return 0 fib(0) = 0.
* elif n == 1: base case untuk 1.
* return 1 fib(1) = 1.
* return fib(n-1) + fib(n-2) rumus Fibonacci rekursif.
* allFib(4) memanggil fungsi (output: 0: 0, 1: 1, 2: 1, 3: 2).

**Kompleksitas:** O(2ⁿ) — exponential time, sangat lambat karena menghitung ulang.







###### **10. Fungsi powersOf2(n)**



Fungsi ini mencetak dan menghitung pangkat 2 secara rekursif dengan strategi divide and conquer.



* def powersOf2(n): mendefinisikan fungsi dengan parameter n.
* if n < 1: base case untuk n kurang dari 1.
* return 0 mengembalikan 0.
* elif n == 1: base case untuk n = 1.
* print(1) mencetak 1 (2 pangkat 0).
* return 1 mengembalikan 1.
* else: recursive case untuk n > 1.
* prev = powersOf2(int(n/2)) rekursi dengan n dibagi 2 (integer division).
* print(prev) mencetak nilai sebelumnya.
* curr = prev\*2 menghitung nilai sekarang (kalikan 2).
* print(curr) mencetak nilai sekarang.
* return curr mengembalikan nilai sekarang.
* powersOf2(50) memanggil fungsi (mencetak rantai: 1, 2, 2, 4, 4, 8, 8, ...).

**Kompleksitas:** O(log n) — logaritmik karena n dibagi 2 setiap rekursi.

