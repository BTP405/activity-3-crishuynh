import socket


def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345)  # Replace 'localhost' with your server's IP address
    client_socket.connect(server_address)

    try:
        # Send message to the server
        message = "Hello, server! This is client. Client is sending the file"
        client_socket.sendall(message.encode())
        server_f = open("Mordecai.png", "rb")
        l = server_f.read(1024)

        print('Sending...')
        client_socket.send(l)

        # Receive acknowledgement from server
        data = client_socket.recv(1024)
        print("Received acknowledgementL:", data.decode())
        client_socket.close()

    finally:
        # Clean up connection
        client_socket.close()


if __name__ == "__main__":
    run_client()
