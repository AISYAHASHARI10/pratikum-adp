while True  :
       print("kalkulator sederhana ^^")
       print("pilih operasi yang kamu inginkan : ")
       print("1.penjumlahan")
       print("2.pengurangan")
       print("3.perkalian")
       print("4.pembagian")
       print("5.keluar")
       angka_awal = float(input("masukan angka awal : "))
       angka_akhir = float(input("masukan angka akhir : "))
       pilihan_operasi = int(input("operasi yang diinginkan :"))
       if pilihan_operasi == 1 : 
           penjumlahan = angka_awal+angka_akhir
           print(f"hasil =  {penjumlahan}") 
       elif pilihan_operasi == 2 :
          print(f"hasil =  {perkalian}")
           pengurangan = angka_awal-angka_akhir
           print(f"hasil = {pengurangan}")
       elif pilihan_operasi == 3 :
          perkalian = angka_awal*angka_akhir
       elif pilihan_operasi == 4  :
           if angka_akhir == 0 :
             print ("tidak dapat mekakukan perhitungan pembagian dengan 0 ")
             print ("silahkan masukan ulang angka yang lain^^")
           else :
             pembagian = angka_awal/angka_akhir
             print(f"hasil =  {pembagian}")
       elif pilihan_operasi == 5 :
           print("selesai")  
           break 
       else :
           print("pilihan tidak tersedia, jangan banyak gaya ^^")
       
