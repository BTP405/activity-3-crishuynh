# Implement a client-server file transfer application where the client sends a file to the server using sockets.
# Before transmitting the file, pickle the file object on the client side. On the server side, receive the pickled
# file object, unpickle it, and save it to disk.


# Requirements:
# The client should provide the file path of the file to be transferred.
# The server should specify the directory where the received file will be saved.
# Ensure error handling for file I/O operations, socket connections, and pickling/unpickling.


import socket


def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)  
    server_socket.bind(server_address)
    server_f = open("Mordecai.png", "wb")
    server_socket.listen(1)  

    print("Server listening for incoming connections...")

    while True:
        # Wait for connection
        client_socket, client_address = server_socket.accept()

        try:
            print("Connection to:", client_address)

            # Receive data from client
            data = client_socket.recv(1024)  # size of message to receive; 1024 is maximum
            print("Received:", data.decode())
            while data:
                print("Receiving...")
                server_f.write(data)
                data = client_socket.recv(1024)

            server_f.close()
            # Send acknowledgement back to client
            message = "Message received by the server!"
            print("Done Receiving")
            client_socket.send('Thank you for connecting')
            client_socket.sendall(message.encode())
            client_socket.close()

        finally:
            # Clean up connection
            client_socket.close()


if __name__ == "__main__":
    run_server()
