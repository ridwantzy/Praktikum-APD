# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])

# daftar_hp = {}

# daftar_hp["hp1"] = "inpinik"
# daftar_hp["hp2"] = "samsing"
# daftar_hp["hp3"] = "oddo"
# daftar_hp["hp4"] = "oviv"
# daftar_hp["hp5"] = "pocco"
# daftar_hp["1"] = "eipel"

# print(daftar_hp)
# # for i, j in daftar_hp.items():
# #     print(f"hp {i} mereknya {j}")


# daftar_buku = dict(buku1 = "bioloji", buku2 = "khimia")
# # print (daftar_buku)
# # print(daftar_buku["buku1"])
# # print(daftar_buku["buku2"])
# print(daftar_buku.get("buku2"))

# nilai = {
#     "mtk" : 60,
#     "bindo" : 70,
#     "bingris" : 80,
#     "pisika" : 90,
#     "APD" : 100
# }

# # for i in nilai:
# #     print(i)

# # for i, j in nilai.items():
# #     print(f"nilai dari {i} adalah : {j}")

# nilai.update({"struktur data" : 99})
# nilai.update({"mtk" : 30})
# print(nilai)
# print()
# trashbin = nilai.pop("mtk")
# print(nilai)
# print()
# print(trashbin)

# del nilai["bindo"]
# print()
# print()

# nilai.clear()
# print(nilai)

# print(f"jumlah elemen dari variabel nilai adalah {len(nilai)}")

# buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }

# pinjam = buku.copy()
# print(pinjam)

# key = "apa", "siapa", "dimana"
# value = "gatau"
# jawab_pertanyaan = dict.fromkeys(key, value)
# print(jawab_pertanyaan)

# for i in key.keys():
#     print(i)

# musik = {
#     "chainsmoke" : ["alone", "liliy"],

# }

# for i, j in musik.items():
#     print(f"musik dari {i} adalah :")
#     for song in j:
#         print(song)
#     print("")

mahasiswa = {
101 : {"Nama" : "Aldy", "Umur" : 19},
111 : {"Nama" : "Abdul", "Umur" : 18, "hobi" : ["membaca", "menulis","ngoding"]}
}
for key, value in mahasiswa.items():
   print("ID Mahasiswa : ", key)
   for key_a, value_a in value.items():
      print (key_a, " : ", value_a)
      print("")
print(mahasiswa[111]["hobi"][-1])

