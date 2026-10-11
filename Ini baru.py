print("============================================")
print("             Kalkulator Sederhana           ")
print("============================================")

Angka_pertama = int(input("Masukan angka pertama : "))
Angka_kedua = int(input("Masukan angka kedua : "))

print("""
Apa yang anda inginkan ?
1. Penambahan
2. Pengurangan
3. Perkalian
4. Pembagian
Pastikan anda memasukan angka 1/2/3/4 tanpa text ataupun symbol
""")

Keinginan = int(input("Masukan disini -> "))
print("")

if Keinginan == 1:
    print(f"oke hasil {Angka_pertama} ditambah dengan {Angka_kedua} adalah")
    print(Angka_pertama + Angka_kedua)
elif Keinginan == 2:
    print(f"oke hasil {Angka_pertama} dikurangkan dengan {Angka_kedua} adalah")
    print(Angka_pertama - Angka_kedua)
elif Keinginan == 3:
    print(f"oke hasil {Angka_pertama} dikali dengan {Angka_kedua} adalah")
    print(Angka_pertama * Angka_kedua)
else:
    print(f"oke hasil {Angka_pertama} dibagi dengan {Angka_kedua} adalah")
    print(Angka_pertama / Angka_kedua)

print("")
print("Jika ingin mengulang perhitungan dapat mengulang program, Terimakasih !")