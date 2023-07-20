import time, socket, sys
import random

print("Initialising....\n")
time.sleep(1) #suspends execution for 1 second

s = socket.socket() #creating socket instance
shost = socket.gethostname() #host name of current system
ip = socket.gethostbyname(shost) #ip address of given host name
print(shost, "(", ip, ")\pyn") #printing host name and ip address
host = ip
name = "receiver"
port = 1234
print("Trying to connect to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port)) #connection between host and port
print("Connected...\n") #host and port are now connected..

s_name = s.recv(1024) #will read atmost 1024 bytes
s_name = s_name.decode() #convert from one encoding scheme to desired scheme

print(s_name, "has joined the chat room\n")

while True:

    k=s.recv(1024)
    k=k.decode() 
    k=int(k) #conversion to int datatype
    i=0
    a=[]
    b=""
    message=""
    while i!=k:
       index = s.recv(1024)
       index = index.decode()
       index=int(index)
       message = s.recv(1024)
       message = message.decode()
       f=random.randint(0,4) #f=radom number between 0&4
       if(f==0):
          b="ACK Lost" 
          s.send(b.encode()) #sending message to sender
         
       else:
          b="ACK "+str(index) 
          s.send(b.encode())
          a.insert(index, message) #inserts message in index in list a
          i=i+1 
          
       
    print("The a message received is :", a) #printing message received