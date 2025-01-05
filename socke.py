import socket, sys
host = sys.argv[1]
############## python socke.py 127.0.0.1 80 82 ##############
def scan(port):
    try:
        socke = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socke.connect((host, port))
        global banner
        banner = socke.recv(1024)
        socke.close()
        return True
    except:
        return False
for i in range(int(sys.argv[2]),int(sys.argv[3])):
    if scan(i):
        print("Port", i, "is open:", banner)
    else:
        print(f"Port {i} is closed")