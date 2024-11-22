import os
import json
from prettytable import PrettyTable


"""
=============================================================================================
                                     AKSES DATABASE
=============================================================================================
"""
# Fungsi untuk memuat data dari database.json
def load_data():
    try:
        with open('database.json', 'r') as file:
            return json.load(file)
            
    except FileNotFoundError:
        print("File database.json tidak ditemukan. Menggunakan data default.")
        return {"users": {}, "inventory": {}}

# Fungsi untuk menyimpan data ke database.json
def save_data(data):
    with open('database.json', 'w') as file:
        json.dump(data, file, indent=4)

# Memuat data dari database.json
data = load_data()
daftar_sembako = data["inventory"]
users = data["users"]
admin_username = "admin"
admin_password = "admin"

# Fungsi untuk memeriksa ketersediaan barang
def cek_stok(nama_barang):
    return daftar_sembako[nama_barang]['stok'] > 0

def cek_jumlah(nama_barang, jumlah):
    return jumlah <= daftar_sembako[nama_barang]['stok']

"""
=============================================================================================
                                     FUNGSI CRUD
=============================================================================================
"""

# Fungsi untuk menambah barang
def tambah():
    os.system('cls || clear')
    print("="*50)
    print("Menambah Sembako Baru".center(50))
    print("="*50)
    sembako_baru = input("Masukkan nama sembako: ")
    while True:
        try:
            hargannya = float(input("Masukkan harga sembako: "))
            if hargannya < 0:
                print("Harga tidak boleh negatif, silahkan masukkan harga yang valid")
                continue
            break
        except ValueError:
            print("Input tidak valid, harap masukkan angka untuk harga")
    
    stok = int(input("Masukkan stok sembako: "))
    daftar_sembako[sembako_baru] = {"harga": hargannya, "stok": stok}
    print(f"Barang '{sembako_baru}' dengan harga Rp{hargannya} dan stok {stok} berhasil ditambahkan.")
    
    # Simpan data ke database.json
    save_data({"users": users,"inventory": daftar_sembako})
    input("\n🔙  Tekan enter untuk kembali ke menu...")

# fungsi unutk mengubah data barang
def ubah():
    daftar_sembako_urut = tampilkan()  # Tampilkan daftar barang sembako
    if not daftar_sembako_urut:
        input("\nMaaf tidak ada barang yang bisa diganti...")
        return
    
    while True:
        try:
            ganti_barang = int(input("Masukkan nomor barang yang ingin diganti (0 untuk batal): ")) - 1
            if ganti_barang == -1:
                return
            
            daftar_sembako_list = list(daftar_sembako_urut.items())
            if 0 <= ganti_barang < len(daftar_sembako_list):
                barang_lama = daftar_sembako_list[ganti_barang]
                nama_barang_lama = barang_lama[0]
                
                # Minta input baru untuk barang
                barang_baru = input(f"Masukkan nama barang baru (kosongkan untuk tetap '{nama_barang_lama}'): ")
                if not barang_baru:
                    barang_baru = nama_barang_lama  # Tetap menggunakan nama lama jika input kosong
                
                while True:
                    try:
                        harga_baru = float(input("Masukkan harga barang baru: "))
                        if harga_baru < 0:
                            print("Harga tidak bisa negatif, silahkan masukkan harga yang valid")
                            continue
                        stok_baru = int(input("Masukkan stok barang baru: "))
                        break
                    except ValueError:
                        print("Input tidak valid. Harap memasukkan harga dengan angka")
                
                
                # Hapus barang lama jika nama barang diubah
                if barang_baru != nama_barang_lama:
                    del daftar_sembako[nama_barang_lama]
                
                # Update atau tambahkan barang baru
                daftar_sembako[barang_baru] = {"harga": harga_baru, "stok": stok_baru}
                
                # Simpan data ke database.json
                save_data({"users": users, "inventory": daftar_sembako})
                print(f"Barang '{nama_barang_lama}' berhasil diperbarui menjadi '{barang_baru}' dengan harga Rp{harga_baru} dan stok {stok_baru}.")
                input("\n🔙  Tekan enter untuk kembali ke menu...")
                return 
            else:
                print("Barang tidak ditemukan, harap memasukkan angka barang yang tersedia!😉")
                input("\nKlik enter untuk kembali memilih...")
                return tampilkan(), ubah()
        except ValueError:
            print("Input tidak valid, Harap memasukkan angka yang tersedia!😉")       
            input("\nKlik enter untuk kembali memilih...")
            return tampilkan(), ubah()

# fungsi untuk menghapus barang beserta datannya
def hapus():
    daftar_sembako_urut = tampilkan()
    if not daftar_sembako:
        input("\nMaaf tidak ada barang yang bisa dihapus...")
        return
    
    while True:
        try:
            hapus_barang = int(input("Masukkan nomor barang yang ingin dihapus (0 untuk batal): ")) - 1
            if 0 <= hapus_barang < len(daftar_sembako):
                daftar_sembako_list = list(daftar_sembako_urut.items())
                hapus_item = daftar_sembako_list[hapus_barang]
                del daftar_sembako[hapus_item[0]]  # Hapus dari dictionary
                # Simpan data ke database.json
                save_data({"users": users, "inventory": daftar_sembako})
                print(f"Barang nomor {hapus_barang + 1} berhasil dihapus.")
                input("\n🔙  Tekan enter untuk kembali ke menu...")
                return
            elif hapus_barang == -1:
                return
            else:
                print("Barang tidak ditemukan, harap memasukkan angka barang yang tersedia!😉")
                input("\nKlik enter untuk memilih lagi...")
                return tampilkan(), hapus()
        except ValueError:
            print("Input tidak valid, harap memasukkan angka yang tersedia!😉")
            input("\nKlik enter untuk memilih lagi...")
            return tampilkan(), hapus() 

# Fungsi untuk menampilkan daftar barang
def tampilkan():
    os.system('cls || clear')
    menu = f"""
    ╔════════════════════════════════════════╗
    ║      📊 Pilih Kriteria Sort 📊         ║
    ╠════════════════════════════════════════╣
    ║  ➤ 1. Nama Barang                      ║
    ║  ➤ 2. Harga                            ║
    ║  ➤ 3. Stok                             ║
    ╚════════════════════════════════════════╝
    """
    print(menu)
    
    pilih_kriteria = input("Masukkan pilihan (1/2/3): ")

    if pilih_kriteria == "1":
        # Urutkan berdasarkan nama barang
        daftar_sembako_urut = dict(sorted(daftar_sembako.items()))
    elif pilih_kriteria == "2":
        # Urutkan berdasarkan harga
        daftar_sembako_urut = dict(sorted(daftar_sembako.items(), key=lambda item: item[1]['harga']))
    elif pilih_kriteria == "3":
        # Urutkan berdasarkan stok
        daftar_sembako_urut = dict(sorted(daftar_sembako.items(), key=lambda item: item[1]['stok']))
    else:
        print("Pilihan tidak valid.")
        input("\n🔙  Tekan enter untuk kembali ke menu...")
        return tampilkan()  # Mengembalikan None jika pilihan tidak valid

    os.system('cls || clear')
    print("=" * 50)
    print(" " * 15 + "=== DAFTAR SEMBAKO ===".center(20))
    print("=" * 50)
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Barang", "Harga", "Stok"]
    for nomor, (barang, info) in enumerate(daftar_sembako_urut.items(), start=1):
        harga_formatted = f"Rp {info['harga']}"
        tabel.add_row([nomor, barang,harga_formatted, info['stok']])
        # print(f"{nomor}. {barang} - Rp{info['harga']} (Stok: {info['stok']})")
    # input("\n🔙  Tekan enter untuk kembali ke menu...")
    print(tabel)
    return daftar_sembako_urut  # Mengembalikan daftar yang diurutkan

"""
=============================================================================================
                                      FUNGSI PENJUAL
=============================================================================================
"""

# Fungsi untuk proses pembelian
def proses_pembelian(keranjang, total_belanja):
    while True:
        os.system('cls || clear')
        menu = f"""
    ╔══════════════════════════════════════════════════════════════════════╗
    ║   ==== ==== ==== ==== 📦  PROSES PEMBELIAN  📦 ==== ==== ==== ====   ║
    ╠══════════════════════════════════════════════════════════════════════╣
    ║  1] Tampilkan Semua Barang                                           ║
    ║  2] Pencarian Barang                                                 ║
    ║  3] Lihat Isi Keranjang                                              ║
    ║  4] Selesai Pembelian                                                ║
    ╚══════════════════════════════════════════════════════════════════════╝
    """
        print(menu)

        pilihan = input("Pilih opsi (1/2/3): ")
        
        if pilihan == "1":
            os.system('cls || clear')
            menu = f"""
            ╔════════════════════════════════════════╗
            ║      📊 Pilih Kriteria Sort 📊         ║
            ╠════════════════════════════════════════╣
            ║  ➤ 1. Nama Barang                      ║
            ║  ➤ 2. Harga                            ║
            ║  ➤ 3. Stok                             ║
            ╚════════════════════════════════════════╝
            """
            print(menu)
            
            pilih_kriteria = input("Masukkan pilihan (1/2/3): ")

            if pilih_kriteria == "1":
                # Urutkan berdasarkan nama barang
                daftar_sembako_urut = dict(sorted(daftar_sembako.items()))
            elif pilih_kriteria == "2":
                # Urutkan berdasarkan harga
                daftar_sembako_urut = dict(sorted(daftar_sembako.items(), key=lambda item: item[1]['harga']))
            elif pilih_kriteria == "3":
                # Urutkan berdasarkan stok
                daftar_sembako_urut = dict(sorted(daftar_sembako.items(), key=lambda item: item[1]['stok']))
            else:
                print("Pilihan tidak valid.")
                input("\n🔙  Tekan enter untuk kembali ke menu...")
                continue
                # return None  # Mengembalikan None jika pilihan tidak valid

                # return daftar_sembako_urut

            while True:
                try:
                    os.system('cls || clear')
                    print("=" * 50)
                    print(" " * 15 + "=== DAFTAR SEMBAKO ===".center(20))
                    print("=" * 50)
                    tabel = PrettyTable()
                    tabel.field_names = ["No", "Nama Barang", "Harga", "Stok"]
                    for nomor, (barang, info) in enumerate(daftar_sembako_urut.items(), start=1):
                        harga_formatted = f"Rp{info['harga']}"
                        tabel.add_row([nomor, barang, harga_formatted, info['stok']])
                    print(tabel)
                    if daftar_sembako_urut is None:
                        continue  # Kembali ke menu jika tampilkan mengembalikan None
                    beli_barang = int(input("Masukkan nomor barang yang ingin dibeli (0 untuk batal/kembali): ")) - 1
                    if beli_barang == -1:
                        return proses_pembelian(keranjang, total_belanja)  # Kembali ke menu sebelumnya
                    
                    if 0 <= beli_barang < len(daftar_sembako_urut):
                        barang_dipilih = list(daftar_sembako_urut.items())[beli_barang]
                        nama_barang = barang_dipilih[0]
                        
                        # Cek stok sebelum meminta jumlah
                        if not cek_stok(nama_barang):
                            print(f"\nMaaf, {nama_barang} sudah habis dan tidak bisa dipesan.")
                            input("\n🔙  Tekan enter untuk kembali ke menu...")
                            continue  # Kembali ke awal loop jika barang habis

                        while True:
                            try:
                                jumlah = int(input("Masukkan jumlah (kg/liter/kotak): "))
                                if jumlah <= 0:
                                    print("Jumlah harus lebih dari 0. Silakan coba lagi.")
                                    continue
                                break
                            except ValueError:
                                print("Input tidak valid. Harap masukkan angka untuk jumlah.")

                        # Cek jika jumlah yang diminta melebihi stok
                        if not cek_jumlah(nama_barang, jumlah):
                            print(f"\nMaaf, jumlah yang Anda masukkan melebihi stok {nama_barang} yang tersedia.")
                            input("\nKlik enter untuk kembali memilih...")
                            continue  # Kembali ke awal loop jika jumlah melebihi stok
                        
                        harga_total = barang_dipilih[1]["harga"] * jumlah
                        daftar_sembako[nama_barang]['stok'] -= jumlah
                        
                        # Simpan perubahan ke database.json
                        save_data({"users": users, "inventory": daftar_sembako})
                        
                        # Tambahkan ke keranjang
                        if nama_barang in keranjang:
                            keranjang[nama_barang]['jumlah'] += jumlah  # Tambahkan jumlah jika barang sudah ada
                            keranjang[nama_barang]['harga'] += harga_total  # Update total harga
                        else:
                            keranjang[nama_barang] = {
                                'jumlah': jumlah,
                                'harga': harga_total
                            }

                        total_belanja += harga_total  # Update total belanja


                        os.system('cls || clear')
                        print("=" * 40)
                        print(f"📦  Barang: {nama_barang}")
                        print(f"🔢  Jumlah: {jumlah}")
                        print("✅  Berhasil ditambahkan ke keranjang!")
                        print("=" * 40)
                        input("\n🔙  Tekan enter untuk melanjutkan belanja atau kembali ke menu...")
                        # continue  # Kembali ke menu pembelian setelah menambah barang
                    else:
                        print("Barang tidak ditemukan, silahkan pilih barang yang tersedia!😉")
                        input("\nKlik enter untuk kembali memilih...")
                        continue
                except ValueError:
                    print("Input harus berupa angka. Silahkan coba lagi😉")
                    input("\nKlik enter untuk kembali memilih...")
                    continue
        elif pilihan == "2":
            total_belanja = cari_barang(keranjang, total_belanja)

        elif pilihan == "3":
            tampilkan_keranjang(keranjang)

        elif pilihan == "4":
            total_belanja_pembeli(total_belanja)
            return keranjang, total_belanja # Selesai pembelian
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang tersedia.")
            input("\nKlik enter untuk mencoba lagi...")
            # continue
        
       
def total_belanja_pembeli(total_belanja):
    # Hitung diskon
    diskon = hitung_diskon(total_belanja, username)
    total_setelah_diskon = total_belanja - diskon

    # Hitung persentase diskon
    if total_belanja > 0:
        persentase_diskon = (diskon / total_belanja) * 100
    else:
        persentase_diskon = 0

    os.system('cls || clear')
    print("=" * 65)
    print("           💰  RINCIAN PEMBELIAN  💰           ".center(65))
    print("=" * 65)
    print(f"Total pembelian Anda adalah:               Rp{total_belanja:>10} ")
    print(f"Diskon yang diterapkan:                    Rp{diskon:>10} ({persentase_diskon:.2f}%) ")
    print(f"Total yang harus dibayar setelah diskon:   Rp{total_setelah_diskon:>10} ")
    print("=" * 65)
    print("         🎉 Silahkan melakukan pembayaran! 🎉        ".center(65))
    print("=" * 65 )

    # Simpan riwayat pembelian
    users[username].setdefault("riwayat_pembelian", []).append(keranjang)
    save_data({"users": users, "inventory": daftar_sembako})

    input("\n🔙  Tekan enter untuk kembali ke menu...")
    
def tampilkan_keranjang(keranjang):
    os.system('cls || clear')
    if not keranjang:
        print("=" * 50)
        print("=== KERANJANG ANDA KOSONG ===".center(50))
        print("=" * 50)
        input("\n🔙  Tekan enter untuk kembali ke menu...")
    else:
        print("=" * 60)
        print("📦  Isi Keranjang  📦".center(50))
        print("=" * 60)
        print(f"{'No.':<5} {'Nama Barang':<20} {'Jumlah (pcs)':<15} {'Harga (Rp)':<10}")
        print("=" * 60)
        for nomor, (nama_barang, info) in enumerate(keranjang.items(), start=1):
            print(f"{nomor:<5} {nama_barang:<20} {info['jumlah']:<15} {info['harga']:<10}")
        print("=" * 60)
        input("\n🔙  Tekan enter untuk kembali ke menu...")


def tampilkan_riwayat(username):
    os.system('cls || clear')
    riwayat = users[username].get("riwayat_pembelian", [])
    if not riwayat:
        print("=" * 50)
        print("=== RIWAYAT PEMBELIAN KOSONG ===".center(50))
        print("=" * 50)
    else:
        print("=" * 50)
        print(" " * 15 + "=== RIWAYAT PEMBELIAN ===".center(20))
        print("=" * 50)
        for index, item in enumerate(riwayat, start=1):
            print(f"Pembelian {index}:")
            print("=" * 50)
            for barang, details in item.items():
                jumlah = details['jumlah']
                total_harga = details['harga']
                print(f"{'Barang:':<15} {barang}")
                print(f"{'Jumlah:':<15} {jumlah} pcs")
                print(f"{'Total Harga:':<15} {total_harga}")
                print("-" * 30)  # Garis pemisah antara barang
            print("=" * 50)
    input("\n🔙  Tekan enter untuk kembali ke menu...")

def cari_barang(keranjang, total_belanja):
    os.system('cls || clear') 
    nama_barang = input("Masukkan nama barang yang ingin dicari: ").strip().lower() 
    hasil_cari = {barang: info for barang, info in daftar_sembako.items() if nama_barang in barang.lower()} 
    while True: 
        try: 
            if hasil_cari:
                os.system('cls || clear') 
                print("=" * 40) 
                print("🎯=== Hasil Pencarian ===🎯".center(40))                    
                print("=" * 40) 
                tabel = PrettyTable()
                tabel.field_names = ["No", "Nama Barang", "Harga (Rp)", "Stok"]
                for nomor, (barang, info) in enumerate(hasil_cari.items(), start=1):
                    tabel.add_row([nomor, barang, info['harga'], info['stok']])
                print(tabel)  # Menampilkan tabel hasil pencarian                    
                print("=" * 40)
                
            else: 
                print("Barang tidak ditemukan.") 
                input("\nKlik enter untuk coba lagi2...") 
                return cari_barang(keranjang, total_belanja)

            beli_barang = int(input("Masukkan nomor barang yang ingin dibeli (0 untuk batal): ")) - 1 
            if beli_barang == -1: 
                return total_belanja  # Kembali jika pengguna membatalkan 

            if 0 <= beli_barang < len(hasil_cari): 
                barang_dipilih = list(hasil_cari.items())[beli_barang] 
                nama_barang = barang_dipilih[0] 

                # Cek stok sebelum meminta jumlah 
                if not cek_stok(nama_barang): 
                    print(f"\nMaaf, {nama_barang} sudah habis dan tidak bisa dipesan.") 
                    input("\n🔙  Tekan enter untuk kembali ke menu...") 
                    return total_belanja  # Kembali jika barang habis 

                while True: 
                    try: 
                        jumlah = int(input("Masukkan jumlah (kg/liter/kotak): ")) 
                        if jumlah <= 0: 
                            print("Jumlah harus lebih dari 0. Silakan coba lagi.") 
                            continue 
                        break 
                    except ValueError: 
                        print("Input tidak valid. Harap memasukkan angka untuk jumlah.") 

                # Cek jika jumlah yang diminta melebihi stok 
                if not cek_jumlah(nama_barang, jumlah): 
                    print(f"\nMaaf, jumlah yang Anda masukkan melebihi stok {nama_barang} yang tersedia.") 
                    input("\nKlik enter untuk kembali memilih...") 
                    return total_belanja  # Kembali jika jumlah melebihi stok 

                harga_total = barang_dipilih[1]["harga"] * jumlah 
                daftar_sembako[nama_barang]['stok'] -= jumlah 

                # Simpan perubahan ke database.json 
                save_data({"users": users, "inventory": daftar_sembako}) 

                # Tambahkan ke keranjang 
                if nama_barang in keranjang: 
                    keranjang[nama_barang]['jumlah'] += jumlah  # Tambahkan jumlah jika barang sudah ada 
                    keranjang[nama_barang]['harga'] += harga_total  # Update total harga 
                else: 
                    keranjang[nama_barang] = { 
                        'jumlah': jumlah, 
                        'harga': harga_total 
                        } 

                total_belanja += harga_total  # Update total belanja


                os.system("cls || clear") 
                print("=" * 40) 
                print(f"📦  Barang: {nama_barang}") 
                print(f"🔢  Jumlah: {jumlah}") 
                print("✅  Berhasil ditambahkan ke keranjang!") 
                print("=" * 40) 
                input("\n🔙  Tekan enter untuk melanjutkan belanja atau kembali ke menu...") 
                # return total_belanja  # Kembali setelah pembelian 
            else: 
                print("Barang tidak ditemukan, silahkan pilih barang yang tersedia!") 
                input("\nKlik enter untuk kembali memilih...") 
                continue 
        except ValueError: 
            print("Input harus berupa angka. Silahkan coba lagi.") 
            input("\nKlik enter untuk kembali memilih...") 
            continue 


def hitung_diskon(total_belanja, username):
    diskon = 0
    # Diskon untuk pembeli baru
    if "riwayat_pembelian" not in users[username]:  # Memeriksa apakah pembeli baru
        diskon += total_belanja * 0.05  # Diskon 5% untuk pembeli baru

    # Diskon berdasarkan total belanja
    if total_belanja > 1000000:  # Jika total lebih dari Rp 1.000.000
        diskon += total_belanja * 0.15  # Diskon 15%
    elif total_belanja > 500000:  # Jika total lebih dari Rp 500.000
        diskon += total_belanja * 0.10  # Diskon 10%
    elif total_belanja > 250000:  # Jika total lebih dari Rp 250.000
        diskon += total_belanja * 0.05  # Diskon 5%
    return diskon  # Mengembalikan total diskon


"""
=============================================================================================
                                     MENU UTAMA
=============================================================================================
"""

while True:
    os.system('cls || clear')
    print("=" * 50)
    print(" " * 15 + "📋  MENU LOGIN  📋" + " " * 15)  # Menambahkan spasi untuk center
    print("=" * 50)
    print(" " * 10 + "1. Registrasi")
    print(" " * 10 + "2. Login")
    print(" " * 10 + "3. Keluar")
    print("=" * 50)
    menu = input("Pilih menu (1/2/3): ")

    if menu == "1":
        while True:
            os.system('cls || clear')
            print("="*50)
            print("Register user baru".center(50))
            print("="*50)
            username = input("Masukkan username: ").strip()
            password = input("Masukkan password: ").strip()
            if not username or not password:
                input("Username dan password tidak boleh kosong, enter untuk coba lagi...")
                continue
            elif username in users:
                input("Registrasi gagal! Username sudah digunakan, enter untuk coba lagi...")
            else:
                role = None
                users[username] = {"password": password, "role": "pembeli"}
                save_data({"users": users, "inventory": daftar_sembako})
                os.system('cls || clear')
                print("=" * 60)
                print("🎉🎉🎉  REGISTRASI BERHASIL!  🎉🎉🎉".center(55))
                print("=" * 60)
                print("🌟  Silakan login dengan akun baru Anda 🤩  🌟".center(55))
                print("=" * 60)
                input("\n🔙  Tekan enter untuk kembali ke menu...")
                break
            
        
    elif menu == "2":
        while True:
            os.system('cls || clear')
            print("="*50)
            print("Login".center(50))
            print("="*50)
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            if username == "" or " " in username:
                input("Username tidak boleh kosong dan tidak boleh mengandung spasi, enter untuk coba lagi...")
                continue
            elif username == admin_username and password == admin_password:
                role = "penjual"
                os.system('cls || clear')
                print("=" * 60)
                print("🎉🎉🎉  LOGIN BERHASIL!  🎉🎉🎉".center(55))
                print("=" * 60)
                print(f"🌟  Selamat datang, {role}!  🌟".center(55))
                print("=" * 60)
                input("\n🔙  Tekan enter untuk masuk ke menu CRUD...")
                break
            elif username in users and users[username]["password"] == password:
                role = "pembeli"
                os.system('cls || clear')
                print("=" * 60)
                print("🎉🎉🎉  LOGIN BERHASIL!  🎉🎉🎉".center(55))
                print("=" * 60)
                print(f"🌟  Selamat datang, {role}!  🌟".center(55))
                print("🛒  Anda sekarang dapat berbelanja dengan nyaman!  🛒".center(55))
                print("=" * 60)
                input("\n🔙  Tekan enter untuk masuk ke menu pembeli...")
                break
            else:
                print("Username atau password yang dimasukkan salah, atau silahkan registrasi terlebih dahulu.")
                input("\n🔙  Tekan enter untuk coba lagi...")
                continue

    elif menu == "3":
        os.system('cls || clear')
        print("=" * 65)
        print(" " * 5 + "🌟 Anda Telah Keluar dari Program 🌟".center(40))
        print(" " * 5 + "🙏 Terima Kasih Telah Menggunakan Layanan Kami! 🙏".center(40))
        print("=" * 65)
        break

    else:
        print("\nPilihan tidak valid.")
        input("\n🔙 Tekan enter untuk kembali ke menu...")
        continue

# Menu CRUD untuk penjual
    while role:
        if role == "penjual":
            os.system('cls || clear')
            print("=" * 50)
            print(" " * 10 + "🌟 Menu CRUD Bahan Sembako 🌟".center(30))
            print("=" * 50)
            print(" " * 10 + "1. ➕ Tambah Barang Sembako")
            print(" " * 10 + "2. 📋 Tampilkan Daftar Barang Sembako")
            print(" " * 10 + "3. ✏️ Edit Data Barang Sembako")
            print(" " * 10 + "4. 🗑️ Hapus Barang Sembako")
            print(" " * 10 + "5. 🚪 Keluar")
            print("=" * 50)
            menu = input(" " * 10 + "Pilih opsi (1/2/3/4/5) :  ")
            if menu == "1":
                tambah()
            elif menu == "2":
                tampilkan()
                input("\n🔙Klik enter untuk kembali ke menu...")

            elif menu == "3":
                ubah()
            elif menu == "4":
                hapus()
            elif menu == "5":
                os.system('cls || clear')
                print("=" * 70)
                print(" " * 5 + "✅ Anda Berhasil Keluar dari Menu Penjual ✅".center(40))
                print("=" * 70)
                input(" " * 5 + "🔙 Klik enter untuk Kembali ke Menu Utama...")
                role = None  # Kembali ke menu login
            else:
                print("Pilihan tidak valid.")
                input("\n🔙  Tekan enter untuk mencoba lagi...")

        elif role == "pembeli":
            os.system('cls || clear')
            print("=" * 50)
            print(" " * 10 + "🌟 MENU PEMBELI 🌟".center(25))
            print("=" * 50)
            print(" " * 10 + "1. 🛒 Tampilkan Barang Sembako")
            print(" " * 10 + "2. 💳 Pembelian") 
            print(" " * 10 + "3. 📜 Tampilkan Riwayat Pembelian")
            print(" " * 10 + "4. 🚪 Keluar")
            print("=" * 50)
            menu = input("Pilih opsi (1/2/3/4) : ")
            if menu == "1":
                tampilkan()
                input("\n🔙  Tekan enter untuk kembali ke menu...")      
            elif menu == "2":
                keranjang = {}
                total_belanja = 0
                keranjang, total_belanja = proses_pembelian(keranjang, total_belanja)
            elif menu == "3":
                tampilkan_riwayat(username)
            elif menu == "4":
                os.system('cls || clear')
                print("=" * 65)
                print(" " * 5 + "🚪 Anda Telah Keluar dari Menu Pembeli 🚪".center(50))
                print(" " * 5 + "✨ Terima Kasih Telah Menggunakan Layanan Kami ✨".center(35))
                print("=" * 65)
                input(" " * 5 + "🔙 Klik enter untuk kembali ke Menu Utama...")
                role = None  # Kembali ke menu login
            else:
                print("Pilihan tidak valid. Silakan pilih opsi yang tersedia.")
                input("\n🔙  Tekan enter untuk kembali ke menu...")
     
