import socket as Socket

client = Socket.socket(Socket.AF_INET, Socket.SOCK_STREAM)

client.connect(('localhost', 3000))

while True:
    message = input('Enter a message: ')
    client.send(message.encode())
    data = client.recv(1024)
    print(data.decode())

    if message == 'exit':
        client.close()
        break
