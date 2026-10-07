"""
A. Kenalan
Alat bantu untuk higher-order functions (fungsi yang menerima atau mengembalikan fungsi lain).
"""

# 1. Partial (fungsi parsial)
# Ia berguna saat ingin membuat fungsi baru dari fungsi yang sudah ada, tapi dengan beberapa argumen tetap.
# kita klo selesaikan masalah fungsi pangkat : 
def powertest(base, exp):
    return base ** exp
powertest(4,2)  # ini g efektif.

# Gunakan partial
from functools import partial
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)  # buat fungsi baru dengan exp tetap 2
cube = partial(power, exp=3)    # buat fungsi baru dengan exp tetap 3

print("Hasil square : ", square(4))  # Output: 16
print("Hasil cube : ", cube(4))      # Output: 64
print("Hasil jumlah: ", square(5) + cube(2))  # Output: 25 + 8 = 33


# cth lain
from functools import partial

def kali(a, b):
    return a * b

kali_sepuluh = partial(kali, b=10)
print("\nHasil kali sepuluh: ", kali_sepuluh(4))


# partial digunakan di query database
# user_query = partial(run_query, 
#                      table="users",
#                      columns="id, name, email",
#                      order_by="name"
#                      )

# user_query(filter="age > 18")  # menjalankan query dengan filter tambahan
# user_query(filter="email LIKE '%@example.com'")  # menjalankan query dengan filter tambahan



"""
lru_cache (memoization)
simpan hasil yang sudah dihitung, jadi kalau diminta lagi, 
tinggal ambil dari catatan. Python menyediakannya lewat lru_cache
"""
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

print(fib(30))   # 832040, selesai sangat cepat



"""
SingleDispatch
Satu nama fungsi, banyak versi, dan Python memilih versi yang cocok berdasarkan tipe argumen pertama.
Keunggulan : 
Menambah jenis baru cukup dengan menambah fungsi baru, tanpa menyentuh kode lama
"""
from functools import singledispatch

@singledispatch
def process(data):
    print("Default processing")

@process.register
def _(data: int):
    print(f"Processing integer: {data}")

@process.register
def _(data: list):
    print(f"Processing list of length {len(data)}")

process(10)        # Processing integer: 10
process([1,2,3])   # Processing list of length 3
process("hello")   # Default processing