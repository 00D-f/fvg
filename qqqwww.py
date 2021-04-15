import socket
import pickle
import threading


soc = socket.socket()

soc.bind(("Localhost", 5000))

soc.listen(100)



def clientUser(conn):
    while True:
        data = conn.recv(2048)
        obj = pickle.loads(data)
        if obj["y"] == "+":
            a = str(int(obj["one"]) + int(obj["two"]))
            conn.send(a.encode())
        if obj["y"] == "-":
            a = str(int(obj["one"]) - int(obj["two"]))
            conn.send(a.encode())
        if obj["y"] == "/":
            a = str(int(obj["one"]) // int(obj["two"]))
            conn.send(a.encode())
            if obj["y"] == "*":
                a = str(int(obj["one"]) * int(obj["two"]))
                conn.send(a.encode())
        if not data:
            break

    conn.close()

while True:
    conn, addr = soc.accept()
    print(addr)
    threading.Thread(target=clientUser, args=(conn,)).start()

