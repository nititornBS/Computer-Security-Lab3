from pwn import *
from base64 import b64decode, b64encode
from Crypto.Hash import HMAC, SHA256
from Crypto.Cipher import AES

ip = '172.26.201.17'
port = 2133

io = remote(ip, port)
data1 = io.recvline().decode("utf-8")
io.sendline(str(5))
data1 = io.recvline().decode("utf-8")
data1 = io.recvline().decode("utf-8")
data1 = io.recvline().decode("utf-8")
data1 = io.recvline().decode("utf-8")

key = b'oak1234567890abc'
msg = 'Welcome to the Jungle!'
# hash by the HMAC
def mac(key, message):
    h = HMAC.new(key, message, SHA256)
    return b64encode(h.digest()).decode('utf-8')
token = mac(key, msg.encode())

io.sendline(token.encode())
data1 = io.recvline().decode("utf-8")
data1= io.recvline().decode("utf-8")
data1= io.recvline().decode("utf-8")
print(data1)

nonceb64 = 'DpOK8NIOuSOQlTq+BphKWw=='
header = 'PleaseSendThisToIP21.36.222.155'
nonce = b64decode(nonceb64)
header = str.encode(header)

cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
cipher.update(header)
# calculate an authentication tag
ct, mt = cipher.encrypt_and_digest(msg.encode())
# ciphertext
ct = b64encode(ct).decode('utf-8')
# mac_tag
mt = b64encode(mt).decode('utf-8')

io.sendline(ct.encode())
io.sendline(mt.encode())
response = io.recvall().decode("utf-8")
print(response)
io.close()
