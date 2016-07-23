# -*- coding:utf-8 -*-
import SocketServer


class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        while True:
            print ""
            data = self.request.recv(1024).strip()
            print "{} wrote:".format(self.client_address[0])
            if data == "shutdown":
                print "server shutdown..."
                break
            if not data:
                print "client %s is dead!" % self.client_address[0]
                break
            self.request.sendall(data.upper())


if __name__ == "__main__":
    host = "localhost"       # 主机名，可以是ip,像localhost的主机名,或""
    port = 9999     # 端口
    address = (host, port)

    server = SocketServer.ThreadingTCPServer(address, MyTCPHandler)
    server.serve_forever()

