# JIKA INGIN LOGIN SEBAGAI PEMBELI, MAKA SILAHKAN LAKUKAN REGISTRASI TERLEBIH DAHULU LALU LOGIN.
# JIKA INGIN LOGIN SEBAGAI PENJUAL, MAKA SILAHKAN LANGSUNG LOGIN DENGAN USN:penjual, PW:penjual123.
# HANYA PENJUAL YANG DAPAT MENAMBAH, MENGUBAH, DAN MENGHAPUS BARANG SEMBAKO
import os
sembako_list = [
    {"nama": "Beras 5kg", "harga": 50000},
    {"nama": "Susu", "harga": 10000},
    {"nama": "Kopi", "harga": 5000},
    {"nama": "minyak", "harga" : 27000}
    ]       
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
            print("\nRegistrasi berhasil!, Silahkan login")
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
            sembako_list.append({'nama': sembako_baru, 'harga': float(hargannya)})
            print(f"Barang '{sembako_baru}' dengan harga Rp{hargannya} berhasil ditambahkan.")
            input("\nKlik enter untuk kembali ke menu...")
        elif menu == "2":
            if not sembako_list:
                print("\nTidak ada barang sembako yang tersedia.")
                input("\nKlik enter untuk kembali ke menu...")
            else:
                os.system('cls || clear')
                print("=== Daftar Sembako ===")
                for index, item in enumerate(sembako_list, start=1):
                    print(f"{index}. {item["nama"]} - Rp{item["harga"]}")
                input("\nKlik enter untuk kembali ke menu...")
        elif menu == "3":
            if not sembako_list:
                print("\nTidak ada barang sembako yang tersedia.")
                input("\nKlik enter untuk kembali ke menu...")
            else:
                os.system('cls || clear')
                print("=== Daftar Sembako ===")
                for index, item in enumerate(sembako_list, start=1):
                    print(f"{index}. {item['nama']} - Rp{item['harga']}")
                item_index = int(input("Masukkan nomor barang yang ingin diubah: ")) - 1
                if 0 <= item_index < len(sembako_list):
                    nama_baru = input("Masukkan nama baru: ")
                    harga_baru = input("Masukkan harga baru: ")
                    sembako_list[item_index] = {'nama': nama_baru, 'harga': float(harga_baru)}
                    print(f"Barang nomor {item_index + 1} berhasil diperbarui.")
                    input("\nKlik enter untuk kembali ke menu...")
                else:
                    print("\nBarang tidak ditemukan.")
                    input("\nKlik enter untuk kembali ke menu...")
        elif menu == "4":
            if not sembako_list:
                print("\nTidak ada barang sembako yang tersedia.")
                input("\nKlik enter untuk kembali ke menu...")
            else:
                os.system('cls || clear')
                print("=== Daftar Sembako ===")
                for index, item in enumerate(sembako_list, start=1):
                    print(f"{index}. {item['nama']} - Rp{item['harga']}")
                item_index = int(input("Masukkan nomor barang yang ingin dihapus: ")) - 1
                if 0 <= item_index < len(sembako_list):
                    hapus_itemm = sembako_list.pop(item_index)
                    print(f"Barang '{hapus_itemm['nama']}' berhasil dihapus.")
                    input("\nKlik enter untuk kembali ke menu...")
                else:
                    print("\nBarang tidak ditemukan.")
                    input("\nKlik enter untuk kembali ke menu...")
        elif menu == "5":
            print("\nAnda berhasil Keluar dari program.")
            break
        else:
            print("\nPilihan tidak valid.")
            input("\nKlik enter untuk mencoba lagi...")

    else:
        role == "pembeli"
        os.system('cls || clear')
        print("="*40)
        print("MENU PEMBELI".center(40))
        print("="*40)
        print("1. Tampilkan Barang Sembako")
        print("2. Pembelian")
        print("3. Keluar")
        menu = input("Pilih opsi: ")
        if menu == "1":
            if not sembako_list:
                print("\nTidak ada barang sembako yang tersedia.")
                input("\nKlik enter untuk kembali ke menu...")
            else:
                os.system('cls || clear')
                print("=== Daftar Sembako ===")
                for index, item in enumerate(sembako_list, start=1):
                    print(f"{index}. {item['nama']} - Rp{item['harga']}")
                input("\nKlik enter untuk kembali ke menu...")      
        elif menu == "2":
            total_belanja = 0
            while True:
                os.system('cls || clear')
                print("=== Daftar Sembako ===")
                for index, item in enumerate(sembako_list, start=1):
                    print(f"{index}. {item['nama']} - Rp{item['harga']}")
                item_index = int(input("Masukkan nomor barang yang ingin dibeli (atau 0 untuk selesai): ")) - 1
                if 0 <= item_index < len(sembako_list):
                    jumlah = int(input(f"Masukkan jumlah '{sembako_list[item_index]['nama']}' yang ingin dibeli: "))
                    total_belanja += sembako_list[item_index]['harga'] * jumlah
                    print(f"Barang '{sembako_list[item_index]['nama']}' ditambahkan ke total.")
                    input("\nKlik enter untuk menambah belanjaan atau menyelesaikan belanja...")
                elif item_index == -1:
                    break
                else:
                    print("\nBarang tidak ditemukan, silahkan pilih barang yang tersedia")
                    input("\nKlik enter untuk kembali memilih...")
            print(f"\nTotal pembelian Anda adalah: Rp{total_belanja}")
            input("\nKlik enter untuk kembali ke menu...")
        elif menu == "3":
            print("\nAnda telah Keluar dari program.")
            print("\nTerima kasih telah menggunakan layanan dari kami")
            break
        else:
            print("\nPilihan tidak valid. Silakan pilih opsi yang tersedia.")
            input("\nKlik enter untuk kembali ke menu...")