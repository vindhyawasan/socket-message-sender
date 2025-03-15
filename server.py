import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "0.0.0.0"
port = 12244
s.bind((host,port))
s.listen(5)
socketclient, address = s.accept()
print(f"got the connection {host} : {port} Here i address {address}")
con = True
while con:
    msg = socketclient.recv(1024) #bytes are store 1024
    msg.decode("utf-8")
    print(msg)
    if msg == "quite":
        s.close()