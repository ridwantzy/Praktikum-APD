# input
Nama = input("Masukkan nama barang: ")
Harga = float(input("Masukkan harga barang: "))
Jumlah = int(input("Masukkan jumlah barang: "))
Diskon = float(input("Masukkan diskon(%): "))

# Proses
th1 = Jumlah * Harga
d = th1 * (Diskon / 100)
th2 = th1 - d
sisa_bagi = Diskon % 3

# Output
print(f"""
    Anda membeli {Jumlah} {Nama} dengan harga satuan Rp.{Harga}, total sebelum diskon adalah Rp.{th1},
    total diskon adalah Rp.{d}, dan total yang harus dibayar adalah Rp.{th2}.
    """)
print(f"{Diskon} dibagi dengan 3 sisanya {sisa_bagi}")