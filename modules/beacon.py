import socket

class Beacon:
    def __init__(self, host="127.0.0.1", port="5100"):
        self.host = host
        self.port = int(port)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.sock.bind((self.host, self.port))
            self.sock.listen(5)

        except Exception as e:
            print(e)

        print(f"[Beacon] Bound to {self.host}:{self.port}")

        self.storage = {}

    def listen(self):
        try:
            # Upon a new connection,
            conn, addr = self.sock.accept()
            with conn:
                print( f"[Beacon] [{self.port}] Connection made {addr}" )
                banner = ""
                
                # Fetch incoming data:
                while True:
                    data = conn.recv(512)
                    if data == b"":
                        break

                    banner += data.decode()

                print( f"[Beacon] [{self.port}] Connection ended with {addr}" )

                # Store incoming data:         
                details = str(addr[0]) + ":" + str(self.port)        
                try:
                    self.storage[details].append(banner)
                
                except KeyError:
                    self.storage[details] = [ banner ]

        # Upon error, 
        except Exception as e:
            print(e)
            return 1
        
    # Return logged data.
    def get_data(self):
        return self.storage