import socket
import time
import os
from colorama import Fore,init
init()

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.bind(('localhost',9990))

s.listen(20)

print(Fore.LIGHTBLACK_EX)

n = 0 

for i in (range(101)) :

    print(' \ ' ,n)

    time.sleep(0.01)

    os.system('cls')

    print(' | ' ,n)

    time.sleep(0.01)

    os.system('cls')

    print(' / ' ,n)

    time.sleep(0.01)

    os.system('cls')

    print(' — ' ,n)
        
    time.sleep(0.01)

    os.system('cls')

    n += 1

os.system('cls')

print(Fore.CYAN , 'Sunucu aktif')

print(Fore.LIGHTCYAN_EX , 'İstemci bekleniyor')

while True :

    c , addr = s.accept()

    print(Fore.LIGHTGREEN_EX , f'{addr} Bağlantı sağlandı')

    datas = c.recv(1024)

    f = open('log.txt','wb')

    while datas:

        f.write(datas)

        datas = c.recv(1024)

    f.close()

    print(Fore.GREEN, 'Dosyalar başarıyla alındı')

    continue
