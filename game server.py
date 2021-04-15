import socket
import threading
import pickle

soc = socket.socket()

soc.bind(("localhost", 5000))

soc.listen(5)
pos = {



}

def loh(con, index):
    while True:
        data = con.recv(1024)
        if not data:
            pos.pop(index)
            break

        obj = pickle.loads(data)
        pos[index] = obj
        con.send(pickle.dumps(pos))
    con.close()

i = 0
while True:
    con, ip = soc.accept()
    threading.Thread(target=loh, args=(con, i)).start()
    i += 1