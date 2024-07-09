import socket as Socket

client = Socket.socket(Socket.AF_INET, Socket.SOCK_STREAM)

client.connect(('localhost', 3000))

response = client.recv(1024)

print(response.decode())