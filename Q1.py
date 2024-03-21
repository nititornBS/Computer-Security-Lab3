from pwn import *
from Crypto.Hash import SHA256
ip = '172.26.201.17'
port = 2133

io = remote(ip, port)

data1 = io.recvline().decode("utf-8")

io.sendline(str(1))
data1 = io.recvline().decode("utf-8")
print(data1)
data1 = io.recvline().decode("utf-8")
print(data1)
data1 = io.recvline().decode("utf-8")
print(data1)
UUID = []
Hash=[]
ans=""
for i in range(20):
    data1 = io.recvline().decode("utf-8")
    data1 = data1.split()[2]
    UUID.append(data1)
    h = SHA256.new()
    h.update(data1.encode())
  
    print(h.hexdigest())
    data1 = io.recvline().decode("utf-8")
    data1 = data1.split()[2]
    Hash.append(data1)
    print(Hash[i])
    if h.hexdigest() == Hash[i]:
        ans += "Y"
    else:
        ans+="N"
    print("___________")
data1 = io.recvline().decode("utf-8")
data1 = io.recvline().decode("utf-8")

print(ans)
io.sendline(ans)
data1 = io.recvline().decode("utf-8")
print(data1)
io.close()