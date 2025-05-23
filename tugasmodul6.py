kumpulan_titik = []
print("titik pertama:")
x1 = int(input("x1: "))
y1 = int(input("y1: "))
kumpulan_titik.append([x1, y1])
print("titik kedua:")
x2 = int(input("x2: "))
y2 = int(input("y2: "))
kumpulan_titik.append([x2, y2])

print("titik ketiga:")
x3 = int(input("x3: "))
y3 = int(input("y3: "))
kumpulan_titik.append([x3, y3])

k = (kumpulan_titik[0][0] - kumpulan_titik[1][0])**2 + (kumpulan_titik[0][1] - kumpulan_titik[1][1])**2
l = (kumpulan_titik[1][0] - kumpulan_titik[2][0])**2 + (kumpulan_titik[1][1] - kumpulan_titik[2][1])**2
m = (kumpulan_titik[2][0] - kumpulan_titik[0][0])**2 + (kumpulan_titik[2][1] - kumpulan_titik[0][1])**2


if k == l or l == m or k == m:
    print("ini Segitiga sama kaki")
else:
    print("ini Bukan segitiga sama kaki")
