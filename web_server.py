__author__ = 'swapna'

import socket

HOST, PORT = '',8888

listener_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listener_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
listener_socket.bind((HOST,PORT))
listener_socket.listen(1)
print('Serving HTTP on post %s' % PORT)
while True:
    client_connection, client_Address = listener_socket.accept()
    request = client_connection.recv(1024)

    print(request)
    http_response = b"""\
        HTTP/1.1 200 OK

        Hello, World!"""
    client_connection.sendall(http_response)
    client_connection.close()