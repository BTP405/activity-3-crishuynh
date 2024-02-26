#Real-Time Chat Application with Pickling:

#Develop a simple real-time chat application where multiple clients can communicate with each other via a central server using sockets. 
#Messages sent by clients should be pickled before transmission. The server should receive pickled messages, unpickle them, and broadcast 
#them to all connected clients.

#Requirements:
#Implement separate threads for handling client connections and message broadcasting on the server side.
#Ensure proper synchronization to handle concurrent access to shared resources (e.g., the list of connected clients).
#Allow clients to join and leave the chat room dynamically while maintaining active connections with other clients.
#Use pickling to serialize and deserialize messages exchanged between clients and the server.

import socket


def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "127.0.0.1"  
    server_port = 8000  
    client.connect((server_ip, server_port))

    try:
        while True:
            msg = input("Enter message: ")
            client.send(msg.encode("utf-8")[:1024])

            response = client.recv(1024)
            response = response.decode("utf-8")

            if response.lower() == "closed":
                break

            print(f"Received: {response}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()
        print("Connection to server closed")


run_client()
