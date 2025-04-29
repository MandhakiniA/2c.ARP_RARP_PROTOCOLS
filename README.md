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
![WhatsApp Image 2025-04-29 at 15 47 48_79c5cab8](https://github.com/user-attachments/assets/c44f53ef-a732-4f2f-a596-cb7e0c95b041)
![WhatsApp Image 2025-04-29 at 15 47 22_3707653a](https://github.com/user-attachments/assets/e8ec7d51-7833-4189-8f6d-b5c56e067be9)


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
![WhatsApp Image 2025-04-29 at 16 12 48_2c264105](https://github.com/user-attachments/assets/e7c2eb5f-a5be-4d42-80ab-ec530d33e8b1)
![WhatsApp Image 2025-04-29 at 16 12 20_0d0c40f4](https://github.com/user-attachments/assets/bb307cdc-02bb-4dd5-bbd7-647b1a5b876b)


## RESULT
Thus, the python program for simulating ARP protocols using TCP was successfully executed.
