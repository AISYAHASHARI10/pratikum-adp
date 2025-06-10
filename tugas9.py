import time
import os
from termcolor import colored 
pesan = "    HAPPY EID  "
lebar = 15
total_langkah = 20
delay = 1
pesan_panjang = pesan * 5
i = 0
while i < total_langkah:
    os.system('cls')  
    potongan = pesan_panjang[i:i+lebar]  
    print(colored(potongan, 'black', 'on_yellow'))  
    time.sleep(delay)
    i = i + 1
