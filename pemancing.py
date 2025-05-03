def data_pemancing():
    with open("pemancing.txt", "w") as file:
        while True:
            nama = input("Nama pemancing: ")
            jumlah_ikan = input("Jumlah ikan yang ditangkap: ")
            file.write(f"{nama} - {jumlah_ikan} ikan\n")

            lanjut = input("Ingin input data lagi? (y/n): ").lower()
            if lanjut != 'y':
                break

    print("Data berhasil disimpan ke file pemancing.txt")
data_pemancing()

from pil import Image #type: ignore
import matplotlib.pyplot as plt #type: ignore

img = Image.open("flowchart_memancing.png")
plt.imshow(img)
plt.axis('off')
plt.title("flowchart memancing")
plt.show()
