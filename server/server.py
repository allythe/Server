import socket, time, threading
port = 0
rooms = []

def room(name, port):
    host = socket.gethostbyname(socket.gethostname())

    clients = []
    history = []

    s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    quit = False
    print("[Server Started]", (host,port))

    while not quit:
        try:
            data,  addr = s.recvfrom(255)
            
            if addr not in clients:
                clients.append(addr)
            
            itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

            print("["+addr[0]+"]=["+str(addr[1])+"]=["+itsatime+"]/",end=" ")


            
           
            print(data.decode("utf-8"))



            
            for client in clients:
                if addr != client:
                    s.sendto(data, client)

        except:
            print("\n[ Server stopped]")
            quit = True
    
    s.close()
   

def main(*args):
    print("Server started\n")
   
    rooms=[]
    host = socket.gethostbyname(socket.gethostname())
    
    s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = (host,9089)
    s.bind(server)
    while True:
        data, addr = s.recvfrom(255)
        try:
            port = 9090+ int(data.decode("utf-8"))
            
            
                

            if not port in rooms:
                print("Created room")
                rm = threading.Thread(target = room, args=("tryz", port))
                rm.start()
                rooms.append(port)

            s.sendto(("Connected").encode("utf-8"), addr)
        except:
            warning = "something went wrong"
            s.sendto((warning.encode("utf-8")), addr)
        

if __name__ == '__main__':
    main()
