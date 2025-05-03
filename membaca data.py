def tampilkan_data_pemancing():
        with open("pemancing.txt", "r") as file:
            print("== Data Pemancing ==")
            for baris in file:
                print(baris.strip())
tampilkan_data_pemancing()