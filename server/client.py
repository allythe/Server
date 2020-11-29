
import socket, threading, time


shutdown = False
join = False

def receving (name, sock):
    while not shutdown:
        try:
            while True:
                data,addr = sock.recvfrom(255)
                print(data.decode("utf-8"))
                time.sleep(0.2)
        except:
            pass

host = socket.gethostbyname(socket.gethostname())
port = 0

server = (host, 9089)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)
Connected = False
while Connected == False:
    print("Write number of room")
    port = int(input())
    s.sendto((str(port)).encode("utf-8"), server)
    time.sleep(0.1)
    data, addr = s.recvfrom(255)
    print(data.decode("utf-8"))
    if data.decode("utf-8") == "Connected":
        Connected = True

room = (host, 9090+port)
alias = input("Name: ")

room_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
room_s.bind((host,0))
room_s.setblocking(0)

rT = threading.Thread(target = receving, args = ("RecvThread",room_s))
rT.start()

while shutdown == False:

    if join == False:
        
        room_s.sendto(("["+alias+"] => join chat ").encode("utf-8"),room)
        join = True
    else:
        try:
            message = input()
           # kokoko
            
            if message != "":
                room_s.sendto(("["+alias+"]::"+message).encode("utf-8"), room)
                
              
            time.sleep(0.2)
        except:
            room_s.sendto(("["+alias+"] <= left chat").encode("utf-8"), room)
            shutdown = True
rT.join()
s.close()


