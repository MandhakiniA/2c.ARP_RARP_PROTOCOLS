import socket
s=socket.socket()
s.bind(('localhost',9000))
s.listen(5)
c,addr=s.accept()
address={"6A:08:AA:C2":"192.168.1.100","8A:BC:E3:FA":"192.168.1.99"}
while True:
    nac=c.recv(1024).decode()
    try:
        c.send(address[nac].encode())
    except KeyError:
        c.send("Not found".encode())