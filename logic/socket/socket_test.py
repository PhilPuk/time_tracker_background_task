import socket

class Server():
    def __init__(self, hostName = None, port = None):
        self.host = hostName
        self.port = port

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.s.bind((self.host, self.port))
        self.s.listen(1)

        def connect(self):
            self.conn, self.addr = self.s.accept()
            print(f"Connected to {self.addr}")

        def responeHandler(self):
            pass

        def run(self):
            self.connect()
            while True:
                data = self.conn.recv(1024)
                if not data:
                    break
                print(data.decode("utf-8"))
                
                # Add response handling

            self.conn.close()
                