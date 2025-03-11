Pilihan_Paket = {
    1 : 'Ayam = Rp.20.000',
    2 : 'Sapi = Rp.35.000',
    3 : 'Cumi-cumi = Rp.45.000'
}
print(f'pilih paket yang diinginkan : {Pilihan_Paket}')
Paket_tersedia = int(input('Masukan nomor paket yang tersedia : '))
Jarak = float(input('Masukan jarak dari rumah ke restaurant : '))
if Jarak < 1 :
    ongkos_pengiriman = 0
elif 1 <= Jarak <= 3 :
    ongkos_pengiriman = 7000
else :
    ongkos_pengiriman = 15000
harga_paket = [20000, 35000, 45000][Paket_tersedia - 1]
TOTAL_BIAYA = harga_paket + ongkos_pengiriman
print(f'Total biaya akhir : Rp{TOTAL_BIAYA}')