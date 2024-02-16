import socket
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Accept server IP, port, and key from command-line arguments
server_ip = sys.argv[1]
port_number = int(sys.argv[2])
key = sys.argv[3].encode()  

# Prompt the user for a message
message = input("Please enter a message to send to the server: ")
message_bytes = message.encode()

# Pad the message to ensure it is a multiple of 16 bytes
padded_message = pad(message_bytes, AES.block_size)

# Encrypt the message
cipher = AES.new(key, AES.MODE_ECB)  
encrypted_message = cipher.encrypt(padded_message)

# Create a socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, port_number))

# Send the encrypted message
client_socket.send(encrypted_message)

# Close the connection
client_socket.close()
