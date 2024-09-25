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
    
    