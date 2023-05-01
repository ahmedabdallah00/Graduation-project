import socket
import threading

HEADER = 64
PORT = 5050
SERVER =socket.gethostbyname(socket.gethostname())
ADDR =(SERVER , PORT)
FORMAT = "utf-8"
DISCONNECT_MSG ="!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"new {addr} connected")
    conncted =True
    while conncted:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                conncted = False
            print(f"{addr}  {msg}")
            print(f"{msg}")


    conn.close()

def start():
    server.listen()
    print(f"{SERVER}")
    while True:
        conn , addr = server.accept()
        thread = threading.Thread(target = handle_client , args=(conn,addr))
        thread.start()
        print(f"ACTIVE CONNECTIONS ")

print("starting")
start()

print(socket.gethostname())
print(SERVER)