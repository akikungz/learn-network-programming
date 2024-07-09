import socket as Scoket

socket = Scoket.socket(Scoket.AF_INET, Scoket.SOCK_DGRAM)

while True:
    message = input('Type a message: ')
    if message == 'exit':
        break
    socket.sendto(message.encode(), ('localhost', 3000))
    print('Message sent')
    response = socket.recv(1024)
    print(response.decode())