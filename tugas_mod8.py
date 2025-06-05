
data_praktikan = []

file = open("data_totnilai_sementara_pratikan.txt", "r")
for line in file:
    data_baris = []  
    kata = ""
    for huruf in line:
        if huruf == ',' or huruf == '\n':
            data_baris.append(kata)
            kata = ""
        else:
            kata += huruf
    if kata != "":
        data_baris.append(kata)

    nim = data_baris[0]
    nama = data_baris[1]
    totpretest = int(data_baris[2])
    totpostest = int(data_baris[3])
    tottugas = int(data_baris[4])
    data_praktikan.append([nim, nama, totpretest, totpostest, tottugas])
file.close()

file_out = open("data_nilai_akhir.txt", "w")
file_out.write("NIM,Nama,Pretest,Postest,Tugas,Nilai Akhir\n")

for i in range(len(data_praktikan)):
    pre = data_praktikan[i][2] / 7
    post = data_praktikan[i][3] /8
    tugas = data_praktikan[i][4] /3
    nilai_akhir = 0.35 * pre + 0.35 * post + 0.3 * tugas
    data_praktikan[i].append(nilai_akhir)
    file_out.write(f"{data_praktikan[i][0]},{data_praktikan[i][1]},{pre},{post},{tugas},{nilai_akhir:.2f}\n")
file_out.close()


jumlah = len(data_praktikan)
total = 0
nilai_tertinggi = data_praktikan[0][5]
nilai_terendah = data_praktikan[0][5]
praktikan_tertinggi = data_praktikan[0][1]
praktikan_terendah = data_praktikan[0][1]

for i in range(jumlah):
    nilai = data_praktikan[i][5]
    total += nilai
    if nilai > nilai_tertinggi:
        nilai_tertinggi = nilai
        praktikan_tertinggi = data_praktikan[i][1]
    if nilai < nilai_terendah:
        nilai_terendah = nilai
        praktikan_terendah = data_praktikan[i][1]

rata2 = total / jumlah
bawah_rata = 0
for i in range(jumlah):
    if data_praktikan[i][5] < rata2:
        bawah_rata += 1

print("Nilai rata-rata:", round(rata2, 2))
print("Nilai tertinggi:", round(nilai_tertinggi, 2), "oleh", praktikan_tertinggi)
print("Nilai terendah:", round(nilai_terendah, 2), "oleh", praktikan_terendah)
print("Jumlah nilai di bawah rata-rata:", bawah_rata)
