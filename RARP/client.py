import socket
s=socket.socket()
s.connect(('localhost',9000))
while True:
    mac=input("Enter mac address: ")
    s.send(mac.encode())
    print("Logical address",s.recv(1024).decode())