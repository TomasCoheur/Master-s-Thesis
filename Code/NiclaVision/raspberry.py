import socket
import os

# Server configuration
HOST = ''  # Use all available interfaces
PORT = 8080

# Create a socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print('Server listening on port', PORT)

    while True:
        # Accept incoming connection
        conn, addr = server_socket.accept()
        print('Connected by', addr)

        # Receive image data
        with conn:
            print('Receiving image data...')
            image_data = conn.recv(1024)  # Adjust buffer size as needed
            # Save image to file
            with open('received_image.jpg', 'wb') as file:
                file.write(image_data)
            print('Image received and saved as received_image.jpg')
