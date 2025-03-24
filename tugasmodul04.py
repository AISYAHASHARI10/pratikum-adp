n = int(input("tambahkan nilai n : "))
if n < 4:
    print("program tidak bisa dijalankan, n minimal 4")
else:
    total_boom = 0
    nilai_tengah = int((n-1)/2)
    for i in range(n):
        for j in range(n):
            if n % 2 == 1 and i == nilai_tengah  and j == nilai_tengah  :
                print("HORE", end=" "*3)
            elif i == j :
                print(1, end=" "*6)
            elif  (i + j) == (n - 1) :
                print(2, end=" "*6)
            else:
                print("BOOM", end=" "*3)
                total_boom = total_boom + 1
        print(  ) 
print(f"Total BOOM yang muncul adalah = {total_boom}")
