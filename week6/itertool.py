"""
A. Kenalan
Membuat iterator yang efisien dan lazy (nilai dihasilkan satu per satu saat dibutuhkan, tidak disimpan semuanya di memori).
"""

"""
1. Count (hitung tak terbatas)
Ia berguna saat web scraping halaman 1, 2, 3, dst. sampai data habis. Kita tidak tahu jumlah halamannya, 
jadi count(1) cocok dipakai, lalu break saat respons gagal atau tidak ada data lagi.
"""
from itertools import count
for i in count(10, 2):  # 10, 12, 14, ...
    if i > 20: break
    print("Hasil count itertool : ",i)

"""
2. Cycle (ulang terus)
Ia berguna saat ingin menampilkan warna yang berbeda untuk setiap baris tabel, misal merah, biru, hijau.
Mereka diberikan secara bergantian pada item.
"""
from itertools import cycle
colors = ['merah', 'biru', 'hijau']
for i, c in zip(range(8), cycle(colors)):
    print("Hasil cycle :", i, c)


"""
3. Repeat (ulang terus)
Ia berguna saat ingin menampilkan warna yang sama untuk setiap baris tabel, misal merah
"""
from itertools import repeat
for i, c in zip(range(5), repeat('merah')):
    print("Hasil repeat :", i, c)

for msg in repeat("Sulthan", 3):  # ulang 3 kali
    print("Hasil repeat :", msg)


"""
4. Accumulate (akumulasi)
Ia berguna saat ingin menampilkan total sementara dari data yang sedang diproses.
"""
from itertools import accumulate
import operator
data = [1, 2, 3, 4, 5]
print("Hasil accumulate tambah :", list(accumulate(data))) # default: penjumlahan
print("Hasil accumulate perkalian :", list(accumulate(data, operator.mul))) # perkalian
print("Hasil accumulate maksimum :", list(accumulate(data, max))) # maksimum
print("Hasil accumulate minimum :", list(accumulate([5, 3, 8, 2], min))) # minimum


"""
5. Product, Permutation, Combination
Product : pasangan kayak kartesian produk
Permutation : semua susunan 2 elemen, urutan berpengaruh
Combination : semua susunan 2 elemen, urutan tidak berpengaruh
"""
from itertools import product, permutations, combinations
print("List produk : ", list(product([1,2], [5,6])))
print("List permutasi : ", list(permutations([1,2,3,4], 3)))
print("List kombinasi: ", list(combinations([5,6,2,3,4], 2)))


mixer = ['ber', 'bor', 'bar', 'bur']
pixer = ['ing', 'ong']
boxer = [3.45, 4.509, 2.3, 0.9]
brot = ['a', 'b', 'c']

for m, p, b, br in zip(mixer, pixer, boxer, brot):
    print("Hasil zip: mixer:", m, ", pixer:", p, ", boxer:", b, ", brot:", br)

print("Total konfigurasi:", len(list(product(mixer, pixer, boxer, brot))))

