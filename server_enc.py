import socket
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Accept port number and key from command-line arguments
port_number = int(sys.argv[1])
key = sys.argv[2].encode() 

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address and port
server_socket.bind(('', port_number))

# Listen for incoming connections
server_socket.listen(1)

print(f"Server listening on port {port_number}")

while True:
    print("Waiting for a connection...")
    client_socket, address = server_socket.accept()
    print(f"Connection from {address} has been established.")

    encrypted_msg = client_socket.recv(1024)
    cipher = AES.new(key, AES.MODE_ECB)  
    decrypted_msg = unpad(cipher.decrypt(encrypted_msg), AES.block_size)

    print(f"Decrypted message: {decrypted_msg.decode()}")

    client_socket.close()
