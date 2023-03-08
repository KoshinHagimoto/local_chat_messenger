import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/tmp/myapp.sock'
print('connecting to {}'.format(server_address))

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

while True:
    message = input('>>>')
    if not message:
        sock.sendall('quit'.encode())
        break
    sock.sendall(message.encode())
    data = str(sock.recv(4096))
    print('Server response: ' + data)
        
print('closing socket')
sock.close()