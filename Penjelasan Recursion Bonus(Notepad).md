###### **1. Fungsi collectStrings(obj)**



Fungsi rekursif untuk mengumpulkan seluruh nilai bertipe string yang tersembunyi di dalam struktur object bersarang.



* def collectStrings(obj): membuat fungsi bernama collectStrings yang menerima satu parameter berupa object.
* resultArr = \[] menyediakan wadah array kosong sebagai tempat penampungan string.
* for key in obj: menelusuri setiap properti yang ada dalam object satu per satu.
* if type(obj\[key]) is str: memeriksa apakah nilai dari properti tersebut berupa string.
* resultArr.append(obj\[key]) memasukkan string yang ditemukan ke dalam wadah penampungan.
* if type(obj\[key]) is dict: memeriksa apakah nilai berupa object lagi (nested).
* resultArr = resultArr + collectStrings(obj\[key]) memanggil diri sendiri untuk menjelajah object dalam, lalu menggabungkan hasilnya.
* return resultArr mengembalikan kumpulan string yang berhasil dikumpulkan.
* obj = {...} membuat contoh data berlapis-lapis dengan string di berbagai kedalaman.
* print(collectStrings(obj)) menjalankan fungsi dan menampilkan \['foo', 'bar', 'baz'].

Kompleksitas: O(n) — n menyatakan total properti di semua tingkatan object.







###### **2. Fungsi stringifyNumbers(obj)**



Fungsi rekursif yang mengubah setiap angka menjadi bentuk string di dalam struktur data bersarang.



* def stringifyNumbers(obj): mendeklarasikan fungsi dengan parameter object.
* newObj = obj menggunakan referensi object yang sama (bukan membuat salinan baru).
* for key in newObj: mengiterasi tiap-tiap kunci yang tersedia.
* if type(newObj\[key]) is int: mendeteksi keberadaan bilangan bulat.
* newObj\[key] = str(newObj\[key]) mengkonversi bilangan menjadi representasi string.
* if type(newObj\[key]) is dict: mendeteksi object bersarang.
* newObj\[key] = stringifyNumbers(newObj\[key]) memproses object dalam secara rekursif.
* return newObj mengembalikan struktur data yang sudah dimodifikasi.
* obj = {...} data uji dengan campuran tipe: angka, array kosong, boolean, dan object bersarang.
* print(stringifyNumbers(obj)) hasilnya seluruh angka menjadi string: '1', '4', '66'.

Kompleksitas: O(n) — bergantung pada jumlah total properti.







###### **3. Fungsi capitalizeWords(arr)**



Fungsi rekursif yang mengubah setiap kata menjadi huruf kapital semua.



* def capitalizeWords(arr): membuat fungsi yang menerima daftar kata.
* result = \[] menyiapkan tempat penyimpanan hasil.
* if len(arr) == 0: mengecek apakah daftar sudah habis.
* return result mengembalikan hasil kosong sebagai titik berhenti.
* result.append(arr\[0].upper()) mengambil kata pertama, mengkapitalisasi seluruh hurufnya, lalu menyimpannya.
* return result + capitalizeWords(arr\[1:]) menggabungkan hasil sekarang dengan pemrosesan sisa daftar.
* words = \['i', 'am', 'learning', 'recursion'] contoh masukan dengan huruf kecil.
* print(capitalizeWords(words)) keluaran: \['I', 'AM', 'LEARNING', 'RECURSION'].

Kompleksitas: O(n×m) — n jumlah kata, m rata-rata panjang tiap kata.







###### **4. Fungsi nestedEvenSum(obj, sum=0)**



Fungsi rekursif untuk menjumlahkan semua bilangan genap yang tersebar dalam object bersarang.



* def nestedEvenSum(obj, sum=0): fungsi dengan akumulator default 0.
* for key in obj: menjelajahi setiap properti object.
* if type(obj\[key]) is dict: bila menemukan object dalam.
* sum += nestedEvenSum(obj\[key]) memanggil diri sendiri dan menambahkan hasilnya ke akumulator.
* elif type(obj\[key]) is int and obj\[key]%2==0: bila menemukan bilangan bulat dan habis dibagi 2.
* sum+=obj\[key] menambahkan bilangan genap ke total.
* return sum mengembalikan jumlah akhir.
* obj1 dan obj2 dua contoh data dengan pola berbeda-beda.
* print(nestedEvenSum(obj1)) hasil 6 (2+2+2).
* print(nestedEvenSum(obj2)) hasil 10 (2+2+2+2+2).

Kompleksitas: O(n) — n total properti di semua kedalaman.







###### **5. Fungsi capitalizeFirst(arr)**



Fungsi rekursif yang hanya mengubah huruf pertama tiap kata menjadi besar.



* def capitalizeFirst(arr): deklarasi fungsi dengan parameter array.
* result = \[] wadah untuk hasil sementara.
* if len(arr) == 0: kondisi berhenti ketika tidak ada lagi kata.
* return result mengembalikan array kosong.
* result.append(arr\[0]\[0].upper() + arr\[0]\[1:]) mengambil huruf pertama saja yang dibesarkan, digabung dengan sisa kata asli.
* return result + capitalizeFirst(arr\[1:]) rekursi dengan elemen berikutnya.
* print(capitalizeFirst(\['car', 'taco', 'banana'])) keluaran: \['Car','Taco','Banana'].

Kompleksitas: O(n×m) — mirip dengan capitalizeWords.







###### **6. Fungsi flatten(arr)**



Fungsi rekursif untuk meratakan array bertingkat-tingkat menjadi satu dimensi.



* def flatten(arr): membuat fungsi penerima array.
* resultArr = \[] menyiapkan hasil berupa array datar.
* for custItem in arr: mengunjungi tiap elemen.
* if type(custItem) is list: mendeteksi elemen yang masih berupa array.
* resultArr.extend(flatten(custItem)) memanggil diri sendiri dan menyebarkan hasilnya.
* else: bila elemen sudah berupa nilai tunggal.
* resultArr.append(custItem) memasukkan langsung ke hasil.
* return resultArr mengembalikan array yang sudah rata.
* Empat contoh pemanggilan dengan tingkat kedalaman berbeda-beda, semuanya menghasilkan \[1, 2, 3, 4, 5] atau \[1, 2, 3].

Kompleksitas: O(n) — n total elemen di semua tingkatan.







###### **7. Fungsi someRecursive(arr, cb)**



Fungsi rekursif yang mengecek apakah minimal satu elemen memenuhi syarat fungsi callback.



* def someRecursive(arr, cb): fungsi dengan parameter array dan fungsi pemeriksa.
* if len(arr) == 0: bila array sudah habis.
* return False artinya tidak ada yang cocok.
* if not(cb(arr\[0])): bila elemen pertama tidak lolos pemeriksaan.
* return someRecursive(arr\[1:], cb) lanjut memeriksa elemen selanjutnya.
* return True elemen pertama lolos, langsung berhenti dengan hasil positif.
* def isOdd(num): pembuat fungsi callback contoh.
* num%2==0 mendeteksi bilangan genap.
* Tiga contoh pemanggilan menunjukkan perilaku short-circuit.

Kompleksitas: O(n) — terburuk memeriksa semua, terbaik berhenti di elemen pertama.







###### **8. Fungsi isPalindrome(strng)**



Fungsi rekursif untuk memeriksa kesamaan string dibaca dari depan dan belakang.



* def isPalindrome(strng): deklarasi fungsi penerima string.
* if len(strng) == 0: string kosong dianggap palindrome.
* return True hasil positif.
* if strng\[0] != strng\[len(strng)-1]: membandingkan karakter ujung depan dan belakang.
* return False bila berbeda, bukan palindrome.
* return isPalindrome(strng\[1:-1]) memeriksa substring tanpa karakter ujung.
* Lima contoh: 'awesome' dan 'foobar' bukan, 'tacocat' dan 'amanaplanacanalpanama' adalah palindrome.

Kompleksitas: O(n) — n panjang string.







###### **9. Fungsi reverse(strng)**



Fungsi rekursif untuk membalik urutan karakter string.



* def reverse(strng): membuat fungsi pembalik.
* if len(strng) <= 1: bila string sangat pendek.
* return strng tidak perlu dibalik.
* return strng\[len(strng)-1] + reverse(strng\[0:len(strng)-1]) mengambil karakter terakhir, letakkan di depan, sisa string dibalik secara rekursif.
* print(reverse('python')) menghasilkan 'nohtyp'.
* print(reverse('appmillers')) menghasilkan 'srellimppa'.

Kompleksitas: O(n²) — operasi slicing memerlukan waktu linear tiap panggilan.







###### **10. Fungsi fib(num)**



Fungsi rekursif naif untuk menghitung bilangan Fibonacci.



* def fib(num): deklarasi fungsi Fibonacci.
* if (num < 2): kondisi dasar deret.
* return num fib(0)=0, fib(1)=1.
* return fib(num - 1) + fib(num - 2) menjumlahkan dua nilai Fibonacci sebelumnya.
* print(fib(4)) hasil 3.
* print(fib(10)) hasil 55.
* print(fib(28)) hasil 317811.
* print(fib(35)) hasil 9227465.

Kompleksitas: O(2ⁿ) — eksponensial, sangat tidak efisien untuk nilai besar.







###### **11. Fungsi recursiveRange(num)**



Fungsi rekursif untuk menjumlahkan bilangan dari num turun ke 0.



* def recursiveRange(num): membuat fungsi penjumlah.
* if num <= 0: bila sudah mencapai atau kurang dari nol.
* return 0 tidak ada yang dijumlahkan.
* return num + recursiveRange(num - 1) menambahkan num dengan jumlah dari num-1, num-2, dst.
* print(recursiveRange(6)) hasil 21 (6+5+4+3+2+1+0).

Kompleksitas: O(n) — linear terhadap nilai masukan.







###### **12. Fungsi productOfArray(arr)**



Fungsi rekursif untuk mengalikan semua angka dalam array.



* def productOfArray(arr): deklarasi fungsi perkalian.
* if len(arr) == 0: bila array sudah kosong.
* return 1 elemen netral perkalian.
* return arr\[0] \* productOfArray(arr\[1:]) mengalikan elemen pertama dengan hasil perkalian sisanya.
* print(productOfArray(\[1,2,3])) hasil 6.
* print(productOfArray(\[1,2,3,10])) hasil 60.

Kompleksitas: O(n) — linear terhadap jumlah elemen.







###### **13. Fungsi factorial(num)**



Fungsi rekursif untuk menghitung faktorial bilangan.



* def factorial(num): membuat fungsi faktorial.
* if num <= 1: kondisi berhenti.
* return 1 definisi faktorial 0 dan 1.
* return num \* factorial(num-1) mengalikan num dengan faktorial num-1.
* print(factorial(1)) hasil 1.
* print(factorial(2)) hasil 2.
* print(factorial(4)) hasil 24.
* print(factorial(7)) hasil 5040.

Kompleksitas: O(n) — linear terhadap nilai num.







###### **14. Fungsi power(base, exponent)**



Fungsi rekursif untuk perhitungan pemangkatan.



* def power(base, exponent): deklarasi dengan dua parameter.
* if exponent == 0: pangkat nol selalu menghasilkan satu.
* return 1 hasil definitif.
* return base \* power(base, exponent-1) mengalikan base dengan hasil pangkat yang lebih kecil satu.
* print(power(2,0)) hasil 1.
* print(power(2,2)) hasil 4.
* print(power(2,4)) hasil 16.

Kompleksitas: O(n) — n adalah nilai exponent.

