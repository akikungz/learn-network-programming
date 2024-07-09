import socket as Socket

socket = Socket.socket(Socket.AF_INET, Socket.SOCK_STREAM)

socket.bind(('0.0.0.0', 3000))
socket.listen(5)

while True:
    connection, address = socket.accept()
    print(f'Connection from {address}')
    connection.send('Hello, {}'.format(address[0]).encode())

    while True:
        data = connection.recv(1024)
        print(data.decode())
        if data.decode() == 'exit':
            connection.close()
            break
