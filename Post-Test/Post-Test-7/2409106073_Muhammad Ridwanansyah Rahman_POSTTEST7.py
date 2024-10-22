# JIKA INGIN LOGIN SEBAGAI PEMBELI, MAKA SILAHKAN LAKUKAN REGISTRASI TERLEBIH DAHULU LALU LOGIN.
# JIKA INGIN LOGIN SEBAGAI PENJUAL, MAKA SILAHKAN LANGSUNG LOGIN DENGAN USN:penjual, PW:penjual123.
# HANYA PENJUAL YANG DAPAT MENAMBAH, MENGUBAH, DAN MENGHAPUS BARANG SEMBAKO
import os
daftar_sembako = {
    "Beras 5kg" : 50000,
    "Susu" : 10000,
    "Kopi" : 5000,
    "Minyak" : 27000,
    "Telur" : 10000
    }   
admin_username = "penjual"
admin_password = "penjual123"
users = {}

# FUNGSI REGISTRASI DAN LOGINN
def input_login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if not username or not password:
        print("Username dan password tidak boleh kosong")
        return input_login()
    return username, password

def input_registrasi():
    username = input("Masukkan username baru: ")
    password = input("Masukkan password baru: ")
    if not username or not password:
        print("Username dan password tidak boleh kosong")
        return input_registrasi()
    return username, password

def verifikasi_login_admin(username, password):
    return username == admin_username and password == admin_password
    
def verifikasi_login_user(username, password):
    return username in users and users[username] == password
    
def tampilkan_pesan_login(role, valid):
    if valid:
        print(f"Login berhasil! Selamat datang, {role}!👋")
    else:
        print("Username atau password yang dimasukkan salah, atau silahkan registrasi terlebih dahulu.")
    return role

def registrasi_user():
    username, password = input_registrasi()
    if username in users:
        print("Registrasi gagal! Username sudah digunakan😞")
    else:
        users[username] = password
        print("Registrasi berhasil! Silakan login dengan akun baru Anda🤩")

# FUNGSI MENU PENJUAL DAN PEMBELI       
def tampilkan():
    if not daftar_sembako:
        print("\nTidak ada barang sembako yang tersedia.")
        return
    else:
        # os.system('cls || clear')
        print("=== Daftar Sembako ===")
        for nomor, (barang, harga) in enumerate(daftar_sembako.items(), start=1):
            print(f"{nomor}. {barang} - Rp{harga}")

def  tambah():
    sembako_baru = input("Masukkan nama sembako: ")
    while True:
        try:
            hargannya = float(input("Masukkan harga sembako: "))
            if hargannya < 0:
                print("Harga tidak boleh negatif, silahkan masukkan harga yang valid")
                continue
            break
        except ValueError:
            print("input tidak valid, harap masukkan angka untuk harga")
    daftar_sembako[sembako_baru] = (hargannya)
    print(f"Barang '{sembako_baru}' dengan harga Rp{hargannya} berhasil ditambahkan.")
    input("\nKlik enter untuk kembali ke menu...")
    
def  ubah():
    tampilkan()
    global daftar_sembako
    if not daftar_sembako:
        input("\nMaaf tidak ada barang yang bisa diganti👍...")
        return
    
    while True:
        try:
            ganti_barang = int(input("Masukkan nomor barang yang ingin diganti(0 untuk batal) : ")) -1
            if ganti_barang == -1:
                return
            elif 0 <= ganti_barang < len(daftar_sembako):
                barang_baru = input("Masukkan barang baru : ")
                while True:
                    try:
                        harga_baru = float(input("Masukkan harga barang baru : "))
                        if harga_baru < 0:
                            print("Harga tidak bisa negatif, silahkan masukkan harga yang valid")
                            continue
                        break
                    except ValueError:
                        print("input tidak valid. Harap memasukkan harga dengan angka")
                daftar_sembako_list = list(daftar_sembako.items())
                daftar_sembako_list[ganti_barang] = (barang_baru, harga_baru)
                daftar_sembako = dict(daftar_sembako_list)
                print(f"Barang nomor {ganti_barang + 1} berhasil diperbarui.")
                input("\nKlik enter untuk kembali ke menu...")
                return 
            else:
                print("Barang tidak ditemukan, harap memasukkan angka barang yang tersedia!😉")
                input("\nKlik enter untuk kembali memilih...")
                return tampilkan(), ubah()
        except ValueError:
            print("Input tidak valid, Harap memasukkan angka yang tersedia!😉")       
            input("\nKlik enter untuk kembali memilih...")
        return tampilkan(), ubah()

def  hapus():
    tampilkan()
    global daftar_sembako
    if not daftar_sembako:
        input("\nMaaf tidak ada barang yang bisa dihapus👍...")
        return
    
    while True:
        try:
            hapus_barang = int(input("Masukkan nomor barang yang ingin dihapus (0 untuk batal dan -1 untuk menghapus semuannya): ")) - 1
            if 0 <= hapus_barang < len(daftar_sembako):
                daftar_sembako_list = list(daftar_sembako.items())
                hapus_itemm = daftar_sembako_list.pop(hapus_barang)
                daftar_sembako = dict(daftar_sembako_list)
                print(f"Barang nomor {hapus_barang +1} berhasil dihapus.")
                input("\nKlik enter untuk kembali ke menu...")
                return
            
            elif hapus_barang == -1:
                return

            elif hapus_barang == -2:
                daftar_sembako.clear()
                print("Anda menghapus semua daftar sembako")
                input("\nKlik enter untuk kembali ke menu...")
                return
            else:
                print("Barang tidak ditemukan, harap memasukkan angka barang yang tersedia!😉")
                input("\nKlik enter untuk memilih lagi...")
                return tampilkan(), hapus()
        except ValueError:
            print("Input tidak valid, harap memasukkan angka yang tersedia!😉")
            input("\nKlik enter untuk memilih lagi...")
            return tampilkan(), hapus() 
        
def keluar_penjual():
    # os.system('cls || clear')
    print("="*40)
    print("Anda berhasil Keluar dari program" .center(40))           
    print("="*40)

def proses_pembelian(keranjang, total_belanja):
    tampilkan()
    while True:
        try:
            nomor_barang = int(input("Masukkan nomor barang yang ingin dibeli (0 untuk selesai): ")) - 1
            if nomor_barang == -1:
                return keranjang, total_belanja

            elif 0 <= nomor_barang < len(daftar_sembako):
                jumlah = int(input("Masukkan jumlah (kg/liter/kotak): "))
                barang = list(daftar_sembako.items())[nomor_barang]
                nama_barang = barang[0]
                harga_total = barang[1] * jumlah
                if nama_barang in keranjang:
                    keranjang[nama_barang] += harga_total
                else:
                    keranjang[nama_barang] = harga_total              
                total_belanja += harga_total
                print("\nKeranjang Belanja: ")
                for barang, total_harga in keranjang.items():
                    print(f"{barang}: Rp{total_harga}")
                print("\nBarang berhasil ditambahkan ke keranjang👌")
                input("\nKlik enter untuk menambah belanjaan atau menyelesaikan belanja...")
                return proses_pembelian(keranjang, total_belanja)
            else:
                print("Barang tidak ditemukan, silahkan pilih barang yang tersedia!😉")
                input("\nKlik enter untuk kembali memilih...")
                return proses_pembelian(keranjang, total_belanja)
        except ValueError:
            print("Input harus berupa angka. Silahkan coba lagi😉")
            input("\nKlik enter untuk kembali memilih...")
            return proses_pembelian(keranjang, total_belanja)

def total_belanja_pembeli():
    # os.system('cls || clear')
    print("="*40)        
    print(f"Total pembelian Anda adalah: Rp{total_belanjaan}" .center(40))
    print("Silahkan melakukan pembayaran!" .center(40))
    print("="*40)
    input("\nKlik enter untuk kembali ke menu...")

def keluar_pembeli():
    # os.system('cls || clear')
    print("="*50)
    print("Anda telah Keluar dari program" .center(45))
    print("Terima kasih telah menggunakan layanan dari kami😊" .center(40))
    print("="*50)

while True:
    # os.system('cls || clear')
    print("="*40)
    print("MENU LOGIN".center(40))
    print("="*40)
    print("1. Registrasi")
    print("2. Login")
    menu = (input("\nPilih menu (1/2): "))

    if menu == "1":
        registrasi_user()
        input("\nKlik enter untuk kembali ke menu...")
        
    elif menu == "2":
        username, password = input_login()
        if verifikasi_login_admin(username, password):
            role = "penjual"
            tampilkan_pesan_login(role, True)
            input("\nKlik enter untuk masuk ke menu CRUD...")
            break
        
        elif verifikasi_login_user(username, password):
            role = "pembeli"
            tampilkan_pesan_login(role, True)
            input("\nKlik enter untuk masuk ke menu pembeli...")
            break
        else:
            tampilkan_pesan_login("", False)
            input("\nKlik enter untuk kembali ke menu...")

    else:
        print("\nPilihan tidak valid.")
        input("\nKlik enter untuk kembali ke menu...")

# Menu CRUD
while role:
    if role == "penjual":
        # os.system('cls || clear')
        print("="*40)
        print("Menu CRUD Bahan Sembako".center(40))
        print("="*40)
        print("1. Tambah Barang Sembako")
        print("2. Tampilkan Barang Sembako")
        print("3. Ubah Barang Sembako")
        print("4. Hapus Barang Sembako")
        print("5. Keluar")
        menu = input("Pilih opsi: ")
        if menu == "1":
            tambah()
        elif menu == "2":
            tampilkan()
            input("\nKlik enter untuk kembali ke menu...")
        elif menu == "3":
            ubah()
        elif menu == "4":
            hapus()
        elif menu == "5":
            keluar_penjual()
            break
        else:
            print("Pilihan tidak valid.")
            input("\nKlik enter untuk mencoba lagi...")

    elif role == "pembeli":
        # os.system('cls || clear')
        print("="*40)
        print("MENU PEMBELI".center(40))
        print("="*40)
        print("1. Tampilkan Barang Sembako")
        print("2. Pembelian")
        print("3. Keluar")
        menu = input("Pilih opsi: ")
        if menu == "1":
            tampilkan()
            input("\nKlik enter untuk kembali ke menu...")      
        elif menu == "2":
            keranjang = {}
            total_belanja = 0
            keranjang, total_belanjaan = proses_pembelian(keranjang, total_belanja)
            total_belanja_pembeli()
        elif menu == "3":
            keluar_pembeli()
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang tersedia.")
            input("\nKlik enter untuk kembali ke menu...")
            