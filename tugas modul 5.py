nilai_x = [-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7]
nilai_fx = []
for x in nilai_x:
    if x > 0:
        fx = x**3 - x
    elif x < 0:
        fx = 1 / (x**2) 
    else:
        fx = 1 
    nilai_fx.append(fx)
print("|   x   |          f(x)          |")
batas = len(nilai_x)
for i in range(batas,batas + 1):
 print("|  " ,nilai_x[0] ," | " ,nilai_fx[0], "  |" )
 print("|  " ,nilai_x[1] ," | " ,nilai_fx[1], " |" )
 print("|  " ,nilai_x[2] ," | " ,nilai_fx[2], "                 |" )
 print("|  " ,nilai_x[3] ," | " ,nilai_fx[3], "               |" )
 print("|  " ,nilai_x[4] ," | " ,nilai_fx[4], "   |" )
 print("|  " ,nilai_x[5] ," | " ,nilai_fx[5], "                 |" )
 print("|  " ,nilai_x[6] ," | " ,nilai_fx[6], "                  |" )
 print("|   " ,nilai_x[7] ," | " ,nilai_fx[7], "                    |" )
 print("|   " ,nilai_x[8] ," | " ,nilai_fx[8], "                    |" )
 print("|   " ,nilai_x[9] ," | " ,nilai_fx[9], "                    |" )
 print("|   " ,nilai_x[10] ," | " ,nilai_fx[10], "                   |" )
 print("|   " ,nilai_x[11] ," | " ,nilai_fx[11], "                   |" )
 print("|   " ,nilai_x[12] ," | " ,nilai_fx[12], "                  |" )
 print("|   " ,nilai_x[13] ," | " ,nilai_fx[13], "                  |" )
 print("|   " ,nilai_x[14] ," | " ,nilai_fx[14], "                  |" )
