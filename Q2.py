from pwn import *
from Crypto.Hash import MD5

ip = '172.26.201.17'
port = 2133

io = remote(ip, port)

def oHash(message):
    message = str.encode(message)
    h = MD5.new(message)
    return h.hexdigest()[:5]

data1 = io.recvline().decode("utf-8")
io.sendline(str(2))
data1 = io.recvline().decode("utf-8")
data1 = io.recvline().decode("utf-8")
data1 = io.recvline().decode("utf-8")
hashpwd = io.recvline().decode("utf-8").strip()  # Strip whitespace
data1 = io.recvline().decode("utf-8")
print(hashpwd)
i = 0
while True:
    pwd = str(i)
    # print(pwd)
    h_5 = oHash(pwd)
    # print("round:", i, "result:", h_5)
   
    if h_5 == hashpwd:
        print(i)
        print("Password Found:", pwd)
        io.sendline(pwd)
        break 
    else:
        i += 1

data1 = io.recvline().decode("utf-8")
print(data1)
flag = io.recvline().decode("utf-8")
print(flag)
io.close()
