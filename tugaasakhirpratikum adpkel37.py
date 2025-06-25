import time
import os
from termcolor import cprint, colored

def clear_screen():
    os.system("cls")

def garis():
    print("=" * 55)

def judul():
    garis()
    cprint("SELAMAT DATANG DI PROGRAM CEK BERAT BADAN IDEAL", "cyan")
    garis()
    print("Program ini membantumu mengetahui status berat badan")
    print("dan memberikan saran diet serta olahraga.")
    garis()


def adalah_float(nilai):
    if len(nilai) == 0:
        return False
    titik = 0
    i = 0
    while i < len(nilai):
        c = nilai[i]
        if c == '.':
            titik += 1
            if titik > 1:
                return False
        if c < '0' or c > '9':
            return False
        i += 1
    return True

def input_pengguna():
    nama = input("Masukkan nama: ")
    gender = input("Masukkan jenis kelamin (L/P): ")

    if gender not in ["L", "l", "P", "p"]:
        cprint("Jenis kelamin harus L atau P.", "red")
        exit()


    tinggi = input("Masukkan tinggi badan dalam cm: ")
    berat = input("Masukkan berat badan dalam kg: ")

    if adalah_float(tinggi) and adalah_float(berat):
        tinggi = float(tinggi)
        berat = float(berat)
    else:
        cprint("Tinggi dan berat harus berupa angka desimal atau bulat. Program berhenti.", "red")
        exit()

    kondisi = input("Ada kondisi khusus (diabetes, alergi, dll)? Jika tidak, ketik tidak: ")
    return nama, gender, tinggi, berat, kondisi

def hitung_bmi(tinggi, berat):
    tinggi_meter = tinggi / 100
    return berat / (tinggi_meter * tinggi_meter)

def status_bmi(bmi):
    if bmi < 18.5:
        return "Kurus"
    elif bmi > 25:
        return "Berlebih"
    else:
        return "Ideal"

def beri_saran(status):
    if status == "Kurus":
        return "Ayo makan yang bergizi dan lebih sering 😄"
    elif status == "Berlebih":
        return "Atur pola makan dan kurangi gorengan 😆"
    else:
        return "Hebat! Gaya hidup sehatmu patut dipertahankan ✨"

def target_berat(status, berat):
    if status == "Kurus":
        return berat + 3
    elif status == "Berlebih":
        return berat - 3
    else:
        return berat

def penjelasan_target(status):
    if status == "Ideal":
        return "Tidak perlu ubah berat badan."
    else:
        return "Disarankan naik/turun 0.5–1 kg per minggu secara sehat."

def saran_diet(status, kondisi):
    if kondisi == "tidak" or kondisi == "TIDAK" or kondisi == "Tidak":
        if status == "Kurus":
            return "Konsumsi kalori sehat seperti alpukat, telur, susu, dan nasi."
        elif status == "Berlebih":
            return "Kurangi gula dan lemak. Perbanyak sayur dan air putih."
        else:
            return "Pertahankan pola makan seimbang dan jam makan teratur."
    else:
        return "Saran diet tidak diberikan. Harap konsultasi ke dokter karena ada kondisi khusus."

def saran_olahraga(status):
    if status == "Kurus":
        return "Lakukan latihan kekuatan seperti push-up atau squat."
    elif status == "Berlebih":
        return "Lakukan jalan cepat atau sepeda 30 menit setiap hari."
    else:
        return "Gabungkan peregangan dan jogging untuk jaga kebugaran."

def animasi():
    for i in [1, 2, 3]:
        titik = "." * i
        print(colored("Menghitung" + titik, "yellow"))
        time.sleep(0.5)

def ulangi():
    tanya = input("Ingin cek lagi? (ya/tidak): ")
    if tanya == "ya" or tanya == "YA" or tanya == "Ya" or tanya == "yA":
        return True
    elif tanya == "tidak" or tanya == "TIDAK" or tanya == "Tidak" or tanya == "tIDAK":
        return False
    else:
        cprint("Mohon jawab dengan 'ya' atau 'tidak'.", "red")
        return ulangi()

def simpan_file(semua_data):
    with open("data_pengguna.txt", "w") as file:
        for data in semua_data:
            file.write(
                "[Nama: " + data[0] +
                " | Gender: " + data[1] +
                " | Tinggi: " + format(data[2], ".2f") + " cm" +
                " | Berat: " + format(data[3], ".2f") + " kg" +
                " | BMI: " + format(data[4], ".2f") +
                " | Status: " + data[5] +
                " | Target Berat: " + format(data[6], ".2f") + " kg]"
                + " === "
            )
    garis()
    cprint("Data pengguna telah disimpan ke file 'data_pengguna.txt'", "yellow")
    garis()

def main():
    clear_screen()
    judul()
    semua_data = []

    while True:
        nama, gender, tinggi, berat, kondisi = input_pengguna()
        animasi()

        bmi = hitung_bmi(tinggi, berat)
        status = status_bmi(bmi)
        saran = beri_saran(status)
        target = target_berat(status, berat)
        penjelasan = penjelasan_target(status)
        diet = saran_diet(status, kondisi)
        olahraga = saran_olahraga(status)

        semua_data.append([nama, gender, tinggi, berat, bmi, status, target])

        garis()
        cprint("Halo " + nama + "!", "green")
        print("BMI kamu:", format(bmi, ".2f"))
        print("Status:", status)
        print("Target berat ideal:", format(target, ".2f"), "kg")
        print("Penjelasan Target:", penjelasan)
        print("Saran:", saran)
        print("Saran Diet:", diet)
        print("Saran Olahraga:", olahraga)
        garis()

        if ulangi():
            clear_screen()
            judul()
        else:
            simpan_file(semua_data)
            cprint("Terima kasih telah menggunakan program ini!", "cyan")
            garis()
            break


main()