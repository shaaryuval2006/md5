import socket
import hashlib
import select
import protocol

class Server:
    def __init__(self):
        self.server_socket = socket.socket()
        self.server_socket.bind(("0.0.0.0", 8000))
        self.server_socket.listen(1)


    def loop(self):
        client_sockets = []
        while 1:
            rlist, _, _ = select.select([self.server_socket]+client_sockets, [], [])
            for current in rlist:
                if current == self.server_socket:
                    client_socket, client_adress = self.server_socket.accept()
                    client_sockets.append(client_socket)
                else:
                    p = protocol.Protocol(current)
                    res, msg = p.get_msg()
                    if not res:
                        client_sockets.remove(current)
                    else:
                        #secret
                        #range
                        #




