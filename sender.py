from cmath import log #math library for complex numbers
from operator import sub #python module for operations
import time, socket, sys

def myfunc(index, msg):
      return (index, msg)

def decimalToBinary(n):  
    return n.replace("0b", "") #replaces all "0b" with ""

def binarycode(s):
    a_byte_array = bytearray(s, "utf8") #returns an array of bytes

    byte_list = []

    for byte in a_byte_array:
        binary_representation = bin(byte) #return binary version
        byte_list.append(decimalToBinary(binary_representation)) #appends binary msg returned by function in byte_list

    a=""
    for i in byte_list: 
        a=a+i
    return a

print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)

s = socket.socket() #creating socket instance
host = socket.gethostname() #host name of current system
ip = socket.gethostbyname(host) #ip address of host name
port = 1234 #port 
s.bind((host, port)) #binds host to port so that it can listen to incoming requests on that IP and port
print(host, "(", ip, ")\n")
name = "sender" 
           
s.listen(1) #specified no of unaccepted connections that system will allow before refusing new connections
print("Waiting for incoming connections...\n")
conn, addr = s.accept() #accepts incoming connection request
print("Received connection from ", addr[0], "(", addr[1], ")\n")

print("connected to the receiver\nEnter x to exit chat room\n")
conn.send(name.encode())

while True:
    message = input(str("Enter Message: ")) #taking message input from user
    if message == "x": #exit condition
        message = "connection closed!"
        conn.send(message.encode())
        print("\n")
        break
    message=binarycode(message)
    print("binary message is: ", message) #printing binary form of entered message
    f=str(len(message)) #length of message in string format
    conn.send(f.encode()) 
   
    i=0
    j=int(input("Enter the window size -> ")) #taking window size input
    
   
    b="" 
   
    j=j-1
    f=int(f)
    k=j

    message_range = range(len(message))

    message = map(myfunc, list(message), message_range) #executes myfunc function for message
    message = list(message) #converting to list form

    substring = message[i:i+(j+1)] #substring

    while i!=f and len(substring) != 0:
        substring = message[i:i+(j+1)]
        for x in substring:  
            conn.send(str(x[1]).encode())
            conn.send(x[0].encode())
            b=conn.recv(1024)
            b=b.decode()
            print(b)
            if(b!="ACK Lost"):
                time.sleep(0.1)
                print("Acknowledgement Received! The sliding window is in the range "+(str(i+1))+" to "+str(k+1)+" Now sending the next packet")
                i=i+1
                k=k+1
                time.sleep(0.1)
            else:
                time.sleep(0.1)
                print("Acknowledgement of the data bit is LOST! The sliding window remains in the range "+(str(i+1))+" to "+str(k+1)+" Now Resending the same packet")
                time.sleep(0.1)
                i=i+1
                k=k+1
                message.append(x)