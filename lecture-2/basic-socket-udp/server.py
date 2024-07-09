import socket as Socket

socket = Socket.socket(Socket.AF_INET, Socket.SOCK_DGRAM)

socket.bind(('0.0.0.0', 3000))

while True:
    data, addr = socket.recvfrom(1024)
    print(f'Connection from {addr}')
    print(data.decode())
    
    socket.sendto(data, addr)