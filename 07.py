def menu():
    print("Menu")
    print("1. Tabel perkalian modulo n")
    print("2. Mencari nilai sigma x")
    print("3. Mencari nilai n!")
    print("4. Total dan rata-rata suatu data")
    print("5. Keluar")

def tabel_modulo():
    while True:
        n = int(input("Masukkan nilai n (0 < n ≤ 10): "))
        if 0 < n <= 10:
            break
        print("Input tidak valid. Coba lagi.")
    
    print(f"Tabel Perkalian Modulo {n}")
    for i in range(n):
        for j in range(n):
            print((i * j) % n, end=" ")
        print()

def sigma_x():
    bawah = int(input("Batas bawah: "))
    atas = int(input("Batas atas: "))
    while atas < bawah:
        print("Batas atas harus lebih besar atau sama dengan batas bawah.")
        bawah = int(input("Batas bawah: "))
        atas = int(input("Batas atas: "))

    total = 0
    for x in range(bawah, atas + 1):
        total += x
    print(f"Jumlah sigma x dari {bawah} sampai {atas} adalah {total}")

def faktorial():
    while True:
        n = int(input("Masukkan nilai n (n ≥ 0): "))
        if n >= 0:
            break
        print("Input tidak valid. Coba lagi.")
    
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    
    print(f"{n}! = {hasil}")

def total_dan_rata_rata():
    while True:
        n = int(input("Masukkan jumlah data (n > 0): "))
        if n > 0:
            break
        print("Jumlah data harus lebih dari 0.")
    
    data = []
    for i in range(n):
        nilai = float(input(f"Data ke-{i + 1}: "))
        data.append(nilai)
    
    total = 0
    for nilai in data:
        total += nilai

    rata_rata = total / n

    print("Data:", data)
    print("Total =", total)
    print("Rata-rata =", rata_rata)

while True:
    menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tabel_modulo()
    elif pilihan == "2":
        sigma_x()
    elif pilihan == "3":
        faktorial()
    elif pilihan == "4":
        total_dan_rata_rata()
    elif pilihan == "5":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
    
    input("Tekan Enter untuk kembali ke menu...")
    print()