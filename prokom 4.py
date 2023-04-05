# print(f"{var/string : < 20}")
# menulis 20 karakter dari kiri ke kanan


# print(f"{var/string : > 20}")
# menulis 20 karakter dari kiri ke kanan

# print(f"{var/string : ^ 20}")
# menulis 20 karakter dengan rata kiri kanan

# membuat tabel data base
pelanggan = []
alamat = []
nohandphone = []

# Sub program masukan pelanggan dibuat oleh budi
def masukpelanggan():
    pelangganBaru = input("masukkan nama pelanggan = ")
    pelanggan.append(pelangganBaru)
    alamatBaru = input("masukkan alamat pelanggan = ")
    alamat.append(alamatBaru)
    nohpBaru = input("masukkan nomor hp = ")
    nohandphone.append(nohpBaru)

# Sub program masukan pelanggan dibuat oleh fani
tampilkandata2 = """
    nama pelanggan      \t: {0}
    alamat pelanggan    \t: {1}
    no. telephone       \t: {2}
"""
def tampilkandata():
    for i in range(0, len(pelanggan)):
        print(tampilkandata2.format(pelanggan[i], alamat[i], nohandphone[i]))

# Program utama dibuat oleh ali
jawaban = input("apakah anda ingin memasukkan data pelanggan (ya/tidak) ? ")

while jawaban in ('ya', 'Ya'):

    masukpelanggan()
    jawaban = input("apakah anda ingin memasukkan data pelanggan (ya/tidak) ?")

tampilkandata()

print("===konversi kilogram ke pound===")
print()
print("kilogram         pound")

for kg in range(0, 20):
    kg = kg + 1
    lb = 2.2
    lb = lb * kg
    print(kg, "-----------", round(lb,2))

for kg in range(0, 20):
    kg = kg + 1
    lb = 2.2
    lb = lb * kg
    print(format(kg, "<5d"), end="")
    print("-----------", format(lb,">5.2f"))