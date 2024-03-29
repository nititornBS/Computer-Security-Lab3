from pwn import *
from Crypto.Cipher import AES
from binascii import hexlify, unhexlify
from itertools import product
from base64 import b64decode, b64encode
from Crypto.Util.Padding import pad


ip = '172.26.201.17'
port = 2133
io = remote(ip, port)
data1 = io.recvline().decode("utf-8")
io.sendline(str(4).encode())
data1 = io.recvline().decode("utf-8")
data1 = io.recvline().decode("utf-8")
hashtext = data1.strip().split(': ')[1]
hashtext = bytes.fromhex(hashtext)

def hash_block(m, prevH):
    cipher = AES.new(m, AES.MODE_ECB)
    return cipher.encrypt(prevH)

cmds = "LAUGH" + " " * 12 + "FLAG"
#on server will add the 11 random key on the front for make it full block
io.sendline(cmds.encode())

added_cmd = " " * 12 + "FLAG"
#I encrypt the  added_cmd with the token(hashtext)
hashans = hash_block(added_cmd.encode(), hashtext)

io.sendline(hashans.hex())

data1 = io.recvline().decode()
print(data1)

response = io.recvall().decode("utf-8")
print(response)


io.close()

