# 2c.SIMULATING ARP /RARP PROTOCOLS
## AIM
To write a python program for simulating ARP protocols using TCP.
## ALGORITHM:
## Client:
1. Start the program
2. Using socket connection is established between client and server.
3. Get the IP address to be converted into MAC address.
4. Send this IP address to server.
5. Server returns the MAC address to client.
## Server:
1. Start the program
2. Accept the socket which is created by the client.
3. Server maintains the table in which IP and corresponding MAC addresses are
stored.
4. Read the IP address which is send by the client.
5. Map the IP address with its MAC address and return the MAC address to client.
## PROGRAM - ARP
### server.py
```python
import socket
s=socket.socket()
s.bind(('localhost',8000))
s.listen(5)
c,addr=s.accept()
address={"165.165.80.80":"6A:08:AA:C2","165.165.79.1":"8A:BC:E3:FA"};
while True:
    ip=c.recv(1024).decode()
    try:
        c.send(address[ip].encode())
    except KeyError:
        c.send("Not Found".encode())
```
### client.py
```python
import socket
s=socket.socket()
s.connect(('localhost',8000))
while True:
    ip=input("Enter logical Address : ")
    s.send(ip.encode())
    print("MAC Address",s.recv(1024).decode())
```
## OUPUT - ARP
![WhatsApp Image 2025-04-29 at 15 47 48_2c1e980a](https://github.com/user-attachments/assets/12ae3638-51ba-4930-9a14-4a7d6621149c)

![WhatsApp Image 2025-04-29 at 15 47 22_18ea530d](https://github.com/user-attachments/assets/d7384052-1f6f-4a07-bfa1-8727b34033f3)

## PROGRAM - RARP
### server.py
```python
import socket
s=socket.socket()
s.bind(('localhost',8000))
s.listen(5)
c,addr=s.accept()
address={"165.165.80.80":"6A:08:AA:C2","165.165.79.1":"8A:BC:E3:FA"};
while True:
    mac=c.recv(1024).decode()
    try:
        c.send(address[mac].encode())
    except KeyError:
        c.send("Not Found".encode())
```
### client.py
```python
import socket
s=socket.socket()
s.connect(('localhost',8000))
while True:
    mac=input("Enter logical address: ")
    s.send(mac.encode())
    print("MAC Address",s.recv(1024).decode())
```
## OUPUT - RARP
![WhatsApp Image 2025-04-29 at 16 12 48_3db0f0f0](https://github.com/user-attachments/assets/86785315-c89f-4def-8f33-29da9964ff82)

![WhatsApp Image 2025-04-29 at 16 12 20_a81ebdcf](https://github.com/user-attachments/assets/c134346e-00c9-40dd-a9b8-a6e9ecd6d02d)

## RESULT
Thus, the python program for simulating ARP protocols using TCP was successfully executed.
