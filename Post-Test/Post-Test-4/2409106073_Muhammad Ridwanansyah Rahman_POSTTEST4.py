# Silahkan login dlu
usn = "Muhammad Ridwanansyah Rahman"
pw = 73 
salah = 1
while salah < 4 :
    username = input("Masukkan username anda : ")
    password = int(input("Masukkan password anda : "))
    if username == usn and password == pw:
        print("Anda berhasil login")
        break
    elif salah < 3:
        print(f"Login gagal, Silahkan coba lagi ")
    else:
        print(f"Login gagal karena anda salah memasukkan username atau password sebanyak {salah} kali")
    salah +=1

if salah == 4 :
    print("Silahkan coba lagi lain waktu")
else:
     while True:
          # input berat badan(mg) & tinggi badan(km) contohnnya 54000000 mg dan 0.00165 km
          berat = float(input("Masukkan berat badan dalam satuan(mg) : "))
          tinggi = float(input("Masukkan tinggi badan dalam satuan(km) : "))

          # proses (menkonfersi, menghitung besaran BMI, dan mengkategorikan)
          berat_badan = berat / 1000000
          tinggi_badan = tinggi * 1000
          bmi = berat_badan / (tinggi_badan * tinggi_badan)
          if bmi < 18.5:
               category = " Anda kekurangan berat badan (Underweight)"
          elif bmi <= 24.9:
               category = "Anda memiliki berat badan yang ideal (Normal)"
          elif bmi <= 29.9: 
               category = "Anda kelebihan berat badan (Overweight)"
          else:
               category = "Anda Obesitas"
          
          # output/hasil berupa besaran BMI dan kategorinya     
          print(f"""
          Indeks massa tubuh (BMI) Anda adalah : {bmi:.1f}
          Kategori : {category}
                """) 
          ulang = input("Apakah anda ingin mencoba lagi (iya/tidak) : ")
          if ulang == "tidak":
                    print("Terima kasih telah mencoba layanan kami")
                    break