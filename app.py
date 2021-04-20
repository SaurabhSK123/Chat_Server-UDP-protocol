import os
import socket
import threading

os.system("tput setaf 2")
os.system("tput bold")
os.system("tput blink")
print("\t\t\t Welcome to Chat Server \n\n ")

os.system("tput sgr0")
os.system("tput bold")
os.system("tput setaf 5")

print("\t\tEnter the Client's system details...\n")
# Receiver IP and port no.
rec_ip=input('\tIP of Receiever : ')
rec_port=int(input('\n\tPort no. of Receiver : '))

print("\t\tEnter your system details....")
# Sender IP and Port no.
s_ip = input('\n\tEnter your IP : ')
s_port =int(input('\n\tEnter port no. of your program : '))


os.system("tput sgr0")
os.system("tput setaf 3")
print("\nStart Chatting....")
#Socket
s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

#Binding IP and port
s.bind( ( s_ip , s_port ) )

def send():
    while True:
        os.system("tput setaf 2")
        os.system("tput bold")
        msg = input()
        s.sendto(msg.encode() ,(rec_ip,rec_port))
def recv():
    while True:
        x = s.recvfrom(1024)
        if x[0].decode() == "bye" or x[0].decode() == "Exit" or x[0].decode() == "Bye":
            s.sendto(b'Bye' , ( rec_ip , rec_port) )
            print("Closing program.. Thank you..")
            os.system("tput sgr0")
            os._exit(1)
        os.system("tput setaf 6")
        os.system("tput bold")
        print("\t\t\t\t\t " +x[0].decode())
        os.system("tput setaf 2")


t1 = threading.Thread( target=send )
t2 = threading.Thread( target=recv )

t1.start()
t2.start()
