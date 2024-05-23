import socket

clientsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host=socket.gethostbyname
port=888
#biding the socket
clientsocket.connect(host, port)
message = clientsocket.recv(1024)
clientsocket.close()
#decrypt the message
print(message.decode('ascii'))