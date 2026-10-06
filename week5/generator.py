"""
A. Kenalan
Fungsi biasa memakai return, lalu selesai dan semua hasil dikirim sekaligus. 
Fungsi generator memakai yield, jadi hasilnya dikeluarkan satu per satu dan fungsi bisa "berhenti sebentar" lalu lanjut lagi.
"""

def firstn(n):
    num = 0
    while num < n:
        yield num  #nilai keluar, lalu pause di sini
        num += 1

first_n = firstn(10)  # belum hitung apapun. Nilai baru dihitung pas diminta : 
print(next(first_n))  # Output: 0
print(next(first_n))  # Output: 1
print(next(first_n))  
print(next(first_n))
print(next(first_n))  
print(next(first_n))

"""
Bagus dipakai jika file atau angka yg diproses besar (misal 1 juta baris), karena
kita hanya cetak yang diperlukan saja, tidak perlu menunggu semua data selesai diproses.

Generator hanya bisa dipakai sekali. Setelah habis, ia kosong.
"""


# Di generator ada cara minta nilai lain selain next() : 
# 1. For Loop
for i in firstn(10):
    print("Dengan For Loop angka ke : ", i)

# 2. list(...)
print("Tampil dgn list : ", list(firstn(7)))

# 3. sum(...)
print("Tampil dgn sum : ", sum(firstn(6)))



"""
B. Generator 1 baris dengan ()
"""
a = [x * x for x in range(5)]   # kurung siku -> LIST
b = (x * x for x in range(5))   # kurung biasa -> GENERATOR

for tes in b:
    print(tes)

"""
Isinya sama, yaitu "kuadrat dari 0 sampai 4", tapi sifatnya beda:
a) langsung menghitung semuanya dan menyimpannya: [0, 1, 4, 9, 16].
b) belum menghitung apa pun. Ia baru menghitung satu per satu saat diminta.
"""


def tiga_kata():
    print("mulai")
    yield "satu"
    print("lanjut")
    yield "dua"
    print("selesai")

g = tiga_kata()
for i in tiga_kata():
    print("tiga kata loop:", i)
print("list tiga kata: ", list(tiga_kata()))



#Pipeline generator,baca dari kanan.

def angka(n):
    for i in range(n):
        yield i

def tambah_sepuluh(data):
    for d in data:
        yield d + 10

def ambil_kelipatan_3(data):
    for d in data:
        if d % 3 == 0:
            yield d

hasil = ambil_kelipatan_3(tambah_sepuluh(angka(8)))
for h in hasil:
    print(h)
#output : 12 dan 15


"""
LATIHAN SOAL!!
Sebuah toko online mencatat 1 juta nomor pesanan. Tim IT hanya ingin memproses nomor yang habis dibagi 5, 
dan tidak mau memenuhi memori. Buat generator nomor_pesanan(n) yang mengeluarkan angka 1 sampai n, 
lalu generator kedua kelipatan_lima(nomor) yang menyaringnya. 
Rangkai keduanya dalam pipeline dan tampilkan 5 hasil pertama saja.
"""
def nomor_pesanan(n):
    for i in range(1, n+1):
        yield i

def kelipatan_lima(nomor):
    for i in nomor:
        if i % 5 == 0:
            yield i

hasil_pertama = kelipatan_lima(nomor_pesanan(1000000))
for i in range(5):
    print("5 hasil pertama generator toko online:", next(hasil_pertama))