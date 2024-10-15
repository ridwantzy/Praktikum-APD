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
users = [] 
while True:
    os.system('cls || clear')
    print("="*40)
    print("MENU LOGIN".center(40))
    print("="*40)
    print("1. Registrasi")
    print("2. Login")
    menu = (input("\nPilih menu (1/2): "))
    if menu == "1":
         username = input("Masukkan username: ")
         password = input("Masukkan password: ")
         if any(user[0] == username for user in users):
             print("Username sudah terdaftar.")
             input("\nKlik enter untuk kembali ke menu...")
         else:
            users.append([username, password])
            print("\nRegistrasi berhasil!, Silahkan login!!")
            input("\nKlik enter untuk kembali ke menu...")
    elif menu == "2":
         username = input("Masukkan username: ")
         password = input("Masukkan password: ")
         user = next((u for u in users if u[0] == username and u[1] == password), None)
         if username == "penjual" and password == "penjual123":
              role = "penjual"
              print("\nSelamat datang penjual")
              input("\nKlik enter untuk masuk ke menu CRUD...")
              break
         elif user:
             role = "pembeli"
             print(f"\nSelamat datang, {username}!")
             input("\nKlik enter untuk masuk ke menu pembeli...")
             break
         else:
            print("Username atau password yang dimasukkan salah, atau silahkan registrasi terlebih dahulu.")
            input("\nKlik enter untuk kembali ke menu...")
    else:
        print("\nPilihan tidak valid.")
        input("\nKlik enter untuk kembali ke menu...")

# Menu CRUD
while role:
    if role == "penjual":
        os.system('cls || clear')
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
            sembako_baru = input("Masukkan nama sembako: ")
            hargannya = input("Masukkan harga sembako: ")
            daftar_sembako[sembako_baru] = float(hargannya)
            print(f"Barang '{sembako_baru}' dengan harga Rp{hargannya} berhasil ditambahkan.")
            input("\nKlik enter untuk kembali ke menu...")
        elif menu == "2":
            if not daftar_sembako:
                print("\nTidak ada barang sembako yang tersedia.")
                input("\nKlik enter untuk kembali ke menu...")
            else:
                os.system('cls || clear')
                print("=== Daftar Sembako ===")
                for nomor, (barang, harga) in enumerate(daftar_sembako.items(), start=1):
                    print(f"{nomor}. {barang} - Rp{harga}")
                input("\nKlik enter untuk kembali ke menu...")
        elif menu == "3":
            if not daftar_sembako:
                print("\nTidak ada barang sembako yang tersedia.")
                input("\nKlik enter untuk kembali ke menu...")
            else:
                os.system('cls || clear')
                print("=== Daftar Sembako ===")
                for nomor, (barang, harga) in enumerate(daftar_sembako.items(), start=1):
                    print(f"{nomor}. {barang} - Rp{harga}")
                ganti_barang = int(input("Masukkan nomor barang yang ingin diganti : ")) -1
                if 0 <= ganti_barang < len(daftar_sembako):
                    barang_baru = input("Masukkan barang baru : ")
                    harga_baru = float(input("Masukkan harga barang baru : "))
                    daftar_sembako_list = list(daftar_sembako.items())
                    daftar_sembako_list[ganti_barang] = (barang_baru, harga_baru)
                    daftar_sembako = dict(daftar_sembako_list)
                    print(f"Barang nomor {ganti_barang + 1} berhasil diperbarui.")
                    input("\nKlik enter untuk kembali ke menu...")
                else:
                    print("\nBarang tidak ditemukan.")
                    input("\nKlik enter untuk kembali ke menu...")
        elif menu == "4":
            if not daftar_sembako:
                print("\nTidak ada barang sembako yang tersedia.")
                input("\nKlik enter untuk kembali ke menu...")
            else:
                os.system('cls || clear')
                print("=== Daftar Sembako ===")
                for nomor, (barang, harga) in enumerate(daftar_sembako.items(), start=1):
                    print(f"{nomor}. {barang} - Rp{harga}")
                hapus_barang = int(input("Masukkan nomor barang yang ingin dihapus (0 untuk menghapus semuanya): ")) - 1
                if 0 <= hapus_barang < len(daftar_sembako):
                    daftar_sembako_list = list(daftar_sembako.items())
                    hapus_itemm = daftar_sembako_list.pop(hapus_barang)
                    daftar_sembako = dict(daftar_sembako_list)
                    print(f"Barang nomor {hapus_barang +1} berhasil dihapus.")
                    input("\nKlik enter untuk kembali ke menu...")
                elif hapus_barang == -1:
                    daftar_sembako.clear()
                else:
                    print("\nBarang tidak ditemukan.")
                    input("\nKlik enter untuk kembali ke menu...")
        elif menu == "5":
            os.system('cls || clear')
            print("="*40)
            print("Anda berhasil Keluar dari program" .center(40))           
            print("="*40)
            break
        else:
            print("\nPilihan tidak valid.")
            input("\nKlik enter untuk mencoba lagi...")

    elif role == "pembeli":
        os.system('cls || clear')
        print("="*40)
        print("MENU PEMBELI".center(40))
        print("="*40)
        print("1. Tampilkan Barang Sembako")
        print("2. Pembelian")
        print("3. Keluar")
        menu = input("Pilih opsi: ")
        if menu == "1":
            if not daftar_sembako:
                print("\nTidak ada barang sembako yang tersedia.")
                input("\nKlik enter untuk kembali ke menu...")
            else:
                os.system('cls || clear')
                print("=== Daftar Sembako ===")
                for nomor, (barang, harga) in enumerate(daftar_sembako.items(), start=1):
                    print(f"{nomor}. {barang} - Rp{harga}")
                input("\nKlik enter untuk kembali ke menu...")      
        elif menu == "2":
            keranjang = {}
            total_belanja = 0
            while True:
                os.system('cls || clear')
                print("=== Daftar Sembako ===")
                for nomor, (barang, harga) in enumerate(daftar_sembako.items(), start=1):
                    print(f"{nomor}. {barang} - Rp{harga}")
                nomor_barang = int(input("Masukkan nomor barang yang ingin dibeli (0 untuk selesai): ")) -1
                if 0 <= nomor_barang < len(daftar_sembako):
                    jumlah = int(input("Masukkan jumlah (kg/liter/kotak): "))
                    barang = list(daftar_sembako.items())[nomor_barang]
                    nama_barang = barang[0]
                    harga_total = barang[1] * jumlah
                    if nama_barang in keranjang:
                        keranjang[nama_barang] += harga_total
                    else:
                        keranjang[nama_barang] = harga_total
                    total = 0
                    for value in keranjang.values():
                        total += value
                    print("\nKeranjang Belanja:")
                    for barang, total_harga in keranjang.items():
                        print(f"{barang}: Rp{total_harga}")
                    print("\nBarang berhasil ditambahkan ke keranjang")
                    input("\nKlik enter untuk menambah belanjaan atau menyelesaikan belanja...")
                elif nomor_barang == -1:
                    break
                else:
                    print("\nBarang tidak ditemukan, silahkan pilih barang yang tersedia")
                    input("\nKlik enter untuk kembali memilih...")

            os.system('cls || clear')
            print("="*40)        
            print(f"Total pembelian Anda adalah: Rp{total}" .center(40))
            print("Silahkan melakukan pembayaran!" .center(40))
            print("="*40)
            input("\nKlik enter untuk kembali ke menu...")

        elif menu == "3":
            os.system('cls || clear')
            print("="*50)
            print("Anda telah Keluar dari program" .center(45))
            print("Terima kasih telah menggunakan layanan dari kami" .center(40))
            print("="*50)
            break
        else:
            print("\nPilihan tidak valid. Silakan pilih opsi yang tersedia.")
            input("\nKlik enter untuk kembali ke menu...")