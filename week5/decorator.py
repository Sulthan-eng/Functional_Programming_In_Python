"""
Kayak OOP, bisa bungkus fungsi lain.
Terdapat ide dasar pada poin A dan B
A. Fungsi juga Benda
Di Python, fungsi bisa diperlakukan seperti nilai biasa, seperti angka atau teks. 
Fungsi bisa disimpan di variabel, dikirim ke fungsi lain, dan dikembalikan dari fungsi.
"""
# 1.) fungsi disimpan di variabel
def sapa():
    print("Halo!")

x = sapa      # TANPA tanda kurung
x()           # sekarang x bisa dipanggil seperti sapa


# 2.) fungsi dikirim ke fungsi lain
def panggil(fungsi):
    print("Sebelum fungsi dipanggil")
    fungsi()
    print("Setelah fungsi dipanggil\n")

panggil(sapa)  # kirim fungsi sapa ke fungsi panggil


# contoh lain
def halo():
    print("Halo dari fungsi")

def bungkus(f):
    print("Mulai")
    f()
    print("Selesai\n")

y = halo
bungkus(y)



"""
B.Fungsi Di Dalam Fungsi dan Fungsi yang Mengembalikan Fungsi 
"""
# 1.) Fungsi di dalam fungsi
def luar():
    
    def dalam():
        print("Ini fungsi dalam")
    dalam()  
luar() 
# fungsi dalam hidup di fungsi luar


# 2.) Fungsi boleh mengembalikan fungsi lain
def luar2():
    def dalam2():
        print("Ini fungsi dalam 2\n")
    return dalam2  # TANPA kurung: yang dikembalikan fungsinya, bukan hasil panggilannya

hasil = luar2()  # hasilnya adalah fungsi dalam2
hasil()          # panggil fungsi dalam2 melalui variabel hasil

"""
Jejaknya:

luar() dijalankan: membuat dalam, lalu mengembalikannya. Belum ada yang tercetak.
Fungsi yang dikembalikan disimpan di variabel hasil.
hasil() menjalankan fungsi tersebut, dan baru sekarang teksnya tercetak.

Bedanya dari langkah 1: return dalam mengembalikan resepnya, 
sedangkan return dalam() akan menjalankannya dulu lalu mengembalikan hasilnya.
"""



def buat_salam():
    print("A")
    def salam():
        print("B\n")
    print("C")
    return salam

x = buat_salam()
print("D")
x()
# OUTPUT : ACDB, INGAT! python jalanin kode per line, masuk dulu fungsi buat salam
# yang dicetak A, lalu C, baru keluar dari fungsi buat_salam, lalu cetak D, 
# baru masuk ke fungsi salam dan cetak B



"""
C. Decorator Pertama
Ingat dua ide sebelumnya: fungsi bisa dikirim ke fungsi lain, 
dan fungsi bisa mengembalikan fungsi. Decorator menggabungkan keduanya.
"""
def hias(func):               # menerima sebuah fungsi
    def wrapper():            # membuat fungsi pembungkus
        print("wrapper Sebelum")
        func()                # menjalankan fungsi asli di tengah
        print("wrapper Sesudah\n")
    return wrapper            # mengembalikan pembungkusnya (TANPA kurung)

def sapa():
    print("Halo wrapper!")

sapa = hias(sapa)
sapa()


@hias   #shortcut aja biar cepet, sama aja kayak sapa = hias(sapa)
def sapa():   
    print("Halo decorator!")
print("tes shortcut")
sapa()  



"""
D. *Args dan **Kwargs
Masalahnya Wrapper kita sejauh ini tidak punya parameter. 
Coba pasang hias ke fungsi yang punya parameter:
"""
# @hias
# def sapa(nama):
#     print("Halo", nama)

# sapa("Budi")   # ERROR: TypeError


"""
Butuh wrapper yang bisa menerima parameter apa aja dan terusin ke fungsi asli.
"""
def tampil(*args, **kwargs):
    print(args)
    print(kwargs)

tampil(1, 2, x=3)



# contoh
def hias(func):
    def wrapper(*args, **kwargs):
        print("\nX")
        hasil = func(*args, **kwargs)
        print("Y")
        return hasil
    return wrapper

@hias
def tambah(a, b):
    return a + b

total = tambah(2, 3)
print("total:", total)



"""
E. Decorator yg Bisa Nolak
Wrapper adalah fungsi biasa, jadi ia bisa memutuskan dulu: jalankan fungsi asli, atau jangan.
Taruh IF di wrapper.
"""
toko_buka = False

def cek_buka(func):
    def wrapper(*args, **kwargs):
        if toko_buka:
            return func(*args, **kwargs)
        else:
            print("Toko tutup, tidak bisa beli")
            return 'GAGAL BELI'
    return wrapper

@cek_buka
def beli_barang(nama_barang):
    print("Membeli", nama_barang) 
    return "Sukses beli"

hasil = beli_barang("Buku")
print(hasil)
    


toko_buka2 = True

def cek_buka(func):
    def wrapper(*args, **kwargs):
        if toko_buka2:
            return func(*args, **kwargs)
        else:
            print("Toko tutup, tidak bisa beli")
            return "Ditolak"
    return wrapper

@cek_buka
def beli_barang(nama_barang):
    print("beli", nama_barang) 
    return "Sukses"

hasil = beli_barang("Kopi")
print(hasil)




"""
SOAL : buatlah dekorator untuk cek autentikasi pada suatu fungsi. 
Fungsi yang menggunakan dekorator tersebut akan mengecek terlebih dahulu hak aksesnya.
"""
role = "admin"
print("\nProgram cek autentikasi")
def cek_akses(func):
    def wrapper(*args, **kwargs):
        if role == "admin":
            return func(*args, **kwargs)
        else:
            print("Akses ditolak")
            return "Gagal"
    return wrapper

@cek_akses
def lihat_data():
    print("Melihat data rahasia")
    return "Data rahasia"

role = "user"
hasil = lihat_data()
print("Role user gagal lihat data:", hasil)

role = "admin"
hasil = lihat_data()
print("Role admin berhasil lihat data:", hasil)




"""
SOAL : Perpustakaan kampus punya fungsi pinjam_buku(judul). Hanya anggota berstatus aktif yang boleh meminjam. 
Buat decorator cek_keanggotaan yang memeriksa variabel status_anggota ("aktif" atau "nonaktif"). 
Jika aktif, fungsi berjalan normal. Jika tidak, cetak "Keanggotaan tidak aktif, peminjaman ditolak". 
Pasang ke pinjam_buku, lalu uji dengan kedua status.
"""
status_member = "aktif"
print("\nProgram perpustakaan kampus")

def cek_keanggotaan(func):
    def wrapper(*args, **kwargs):
        if status_member == "aktif":
            return func(*args, **kwargs)
        else:
            print("Keanggotaan tidak aktif, peminjaman ditolak")
            return "Ditolak"
    return wrapper

@cek_keanggotaan
def pinjam_buku(judul):
    print("Minjam buku:", judul)
    return "Sukses minjam"

status_member = "nonaktif"
hasil = pinjam_buku("Python untuk Pemula")
print("Status nonaktif:", hasil)

status_member = "aktif"
hasil = pinjam_buku("Python untuk Pemula")
print("Status aktif:", hasil)


