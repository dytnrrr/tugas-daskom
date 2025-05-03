#pseudocode
print("mulai")
print("buat list untuk menyimpan curah hujan")
print("buat list nama bulan")

print("untuk setiap bulan dalam daftar bulan:")
print("minta input curah hujan")
print("simpan dalam list")

print("hitung total curah hujan")
print("hitung rata-rata curah hujan")
print("nilai tertinggi di bulan ke berapa")
print("nilai terendah di bulan ke berapa")

print("tampilkan:")
print("total curah hujan")
print("rata-rata curah hujan")
print("bulan dengan hujan tertinggi")
print("bulan dengan curah hujan terendah")
print("selesai")



from plt import image # type: ignore
import matplotlib.pyplot as plt # type: ignore

def tampilkan_flowchart():
    img = image.open("flowchart_curah_hujan.png")
    plt.imshow(img)
    plt.axisi('off')
    plt.titlle("flowchart curah hujan")
    plt.show()

def data_curah_hujan():
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
             "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    curah_hujan = []

    print("Masukkan total curah hujan (dalam mm) untuk setiap bulan:")
    for nama_bulan in bulan:
        while True:
            try:
                curah = float(input(f"{nama_bulan}: "))
                if curah < 0:
                    print("Curah hujan tidak boleh negatif. Ulangi.")
                    continue
                curah_hujan.append(curah)
                break
            except ValueError:
                print("Masukkan angka yang valid!")

    total = sum(curah_hujan)
    rata_rata = total / 12
    tertinggi = max(curah_hujan)
    terendah = min(curah_hujan)
    bulan_tertinggi = bulan[curah_hujan.index(tertinggi)]
    bulan_terendah = bulan[curah_hujan.index(terendah)]

    print("\n=== Hasil Analisis Curah Hujan ===")
    print(f"Total curah hujan: {total:.2f} mm")
    print(f"Rata-rata per bulan: {rata_rata:.2f} mm")
    print(f"Curah hujan tertinggi: {tertinggi:.2f} mm ({bulan_tertinggi})")
    print(f"Curah hujan terendah: {terendah:.2f} mm ({bulan_terendah})")

data_curah_hujan()
