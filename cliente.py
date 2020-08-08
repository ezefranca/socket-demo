import socket
from config import UDP_IP, UDP_PORT

# UDP_IP = "127.0.0.1"
# UDP_PORT = 5065

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (UDP_IP, UDP_PORT)
while True:
    print('Digite algo para enviar, para sair digite q')
    msg = input()
    udp.sendto (msg.encode(), dest)
    if msg == 'q':
        udp.close()
        break
udp.close()