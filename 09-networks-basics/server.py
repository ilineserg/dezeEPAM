import json
import socket
import time

host = socket.gethostbyname(socket.gethostname())
port = 9090

users = {}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

quit = False
print('.: Server started :.')

while not quit:
    try:
        data, address = s.recvfrom(1024)

        if address not in users:
            users.update({address: data.decode('utf-8')})

        itsattime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

        print("[" + address[0] + "]=[" + str(address[1]) + "]=[" + itsattime + "]/", end="")
        print(data.decode("utf-8"))

        for user in users:
            if address != user:
                s.sendto(data, user)
    except:
        print("\n[.: Server Stopped :.]")
        quit = True

s.close()
