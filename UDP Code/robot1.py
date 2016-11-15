import SocketServer

class MyUDPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print "{} wrote:".format(self.client_address[0])
        print data

if __name__ == "__main__":
    print "Server for this jimmy has started"
    HOST, PORT = "192.168.0.100", 3100
    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()
	
    print "Hello world"










#import socket
#
#def Main():
#    host = 'localhost'
#    port = 5000
#
#    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    s.bind((host,port))
#
#    print "Server Started."
#    while True:
#        data, addr = s.recvfrom(1024)
#        print "message From: " + str(addr)
#        print "from connected user: " + str(data)
#    c.close()
#
#if __name__ == '__main__':
#    Main()



