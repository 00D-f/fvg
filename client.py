import socket
import pickle


y = input('znack')
one = input ('первое число')
two = input('второе число')

sendObj = {
    'y' : y,
    'one' : one,
    'two' : two
}

soc = socket.socket()

soc.connect(("192.168.71.240", 5000))

soc.send(pickle.dumps(sendObj))
data = soc.recv(1024)

print(data)