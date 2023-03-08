import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/tmp/myapp.sock'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))
sock.bind(server_address)

sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        while True:
            data = connection.recv(4096)
            data_str = data.decode('utf-8')
            if data_str == 'quit':
                break
            print('Received ' + data_str)
            response = 'Processing ' + data_str
            connection.sendall(response.encode())
    finally:
        print("Closing current connection")
        connection.close()