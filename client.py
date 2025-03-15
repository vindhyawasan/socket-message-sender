import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "127.0.0.1"
port = 12244
s.connect((host,port))
con = True
while con:
    msg = input("Enter msg : \n")
    s.send(msg.encode("utf-8"))
    if msg == "quit":
        s.close()