from pwn import *
from Crypto.Hash import MD5

ip = '172.26.201.17'
port = 2133

io = remote(ip, port)

def oHashPlus(message):
    message = str.encode(message)
    h = MD5.new(message)
    return h.hexdigest()[:10]

def find_collision():
    seen_hashes = {}
    while True:
        username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=20))
        hashed_username = oHashPlus(username)
        if hashed_username in seen_hashes:
            if username in seen_hashes[hashed_username]:
                continue
            return seen_hashes[hashed_username], username
        seen_hashes[hashed_username] = username

data1 = io.recvline().decode("utf-8")
io.sendline(str(3))
data1 = io.recvline().decode("utf-8")
data1 = io.recvline().decode("utf-8")
data1 = io.recvline().decode("utf-8")
user1, user2 = find_collision()
print("User1:", user1)
print("User2:", user2)

# Send the found usernames to the server
io.sendline(user1)
io.sendline(user2)

# Receive the response from the server
response = io.recvall().decode("utf-8")
print(response)

# Close the connection
io.close()
