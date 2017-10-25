from socket import *
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

mailserver = 'localhost'
serverport = 25

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, serverport))
recv = clientSocket.recv(1024).decode()
print(recv)
if (recv[:3] != '220'):
    print('220 reply not received from server.')
    
# Send HELO command and print server response.
heloCommand= 'HELO Localhost\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if (recv1[:3] != '250'):
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
mailFromCommand = 'MAIL FROM: <rob@rnwood.co.uk>\r\n'
clientSocket.send(mailFromCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if (recv1[:3] != '250'):
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptToCommand = 'RCPT TO: <rob@rnwood.co.uk>\r\n'
clientSocket.send(rcptToCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if (recv1[:3] != '250'):
    print('250 reply not received from server.')

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if (recv1[:3] != '354'):
    print('354 reply not received from server.')
    
# Send message data.
print("Send message data")
clientSocket.send(msg.encode())

# Message ends with a single period.
print(endmsg)
clientSocket.send(endmsg.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if (recv1[:3] != '250'):
    print('250 reply not received from server.')

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if(recv1[:3] != '221'):
	print('221 reply not received from server')
clientSocket.close()
