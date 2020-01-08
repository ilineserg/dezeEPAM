import json
import socket
import threading
import time


shutdown = False
join = False


def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, address = sock.recvfrom(1024)
                data = data.decode('utf-8')
                print(f'\n{data}')
                time.sleep(0.2)
        except:
            pass


host = socket.gethostbyname(socket.gethostname())
port = 0

server = ("127.0.1.1", 9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

alias = input("Name: ")

rT = threading.Thread(target=receving, args=("RecvThread", s))
rT.start()

while not shutdown:
    if not join:
        s.sendto(f"{alias}".encode("utf-8"), server)
        join = True
    else:
        try:
            message = input('Message: ')

            if message != "":
                s.sendto(f"{alias}: {message}".encode("utf-8"), server)

            time.sleep(0.2)
        except:
            s.sendto(f"{alias} left chat".encode("utf-8"), server)

            shutdown = True

rT.join()
s.close()