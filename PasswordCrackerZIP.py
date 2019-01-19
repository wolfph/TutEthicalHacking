import zipfile
import itertools
import string
from threading import Thread
import traceback
import hashlib

# Directory of the crack file to crack
zipFile = zipfile.ZipFile("CrackFolder.zip")

def bruteforce():
    myLetters = string.ascii_letters + string.digits + string.punctuation
    for i in range(3,10):
        for j in map(''.join, itertools.product(myLetters, repeat=i)):
            t = Thread(target=crack, args=(zipFile, j))
            t.start()

def dictionary():
    #Name of the txt doc which contains the passwords
    passwords = open("john.txt")
    for line in passwords.readlines():
        pwd = line.strip("\n")
        t = Thread(target=crack, args=(zipFile, pwd))
        t.start()

def gen_rainbowtable():
    passwords = open("john.txt")
    output = open("rainbowtable.txt", "w")
    for line in passwords.readlines():
        pwd = line.strip('\n')
        hash = hashlib.sha512(str.encode(pwd))
        output.write(hash.hexdigest() + "#" + pwd + "\n")
    output.close()
    passwords.close()

def crackHash(hash):
    rainbowtable = open("rainbowtable.txt")
    for line in rainbowtable.readlines():
        hashpwd = line.split('#', 1)
        if hash == hashpwd[0]:
            print("Success: Password is " + hashpwd[1])

def crack (zip, pwd):
    try:
        zip.extractall(pwd=str.encode(pwd))
        print('Success: Password is ' + pwd)
    except:
        pass

#bruteforce()
#dictionary()
#gen_rainbowtable()
crackHash("e72ff859807b38201a35d29dc7ec6365118f3bfdadc81fc1be400f0d825194d04826f563e9093949a8fd12fc73d447ea01ca8b73dcdd206836cbb54d5ab79a34")