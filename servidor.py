import socket
import time
from config import UDP_IP, UDP_PORT

# UDP_IP = "127.0.0.1"
# UDP_PORT = 5065

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (UDP_IP, UDP_PORT)
udp.bind(orig)

while True:
    msg, cliente = udp.recvfrom(1024)
    if msg.decode() == 'q':
        udp.close()
        break
    print(cliente, msg.decode())

udp.close()

