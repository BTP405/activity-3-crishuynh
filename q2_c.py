# Distributed Task Queue with Pickling:

# Create a distributed task queue system where tasks are sent from a client to multiple worker nodes for processing
# using sockets.
# Tasks can be any Python function that can be pickled. Implement both the client and worker nodes.
# The client sends tasks (pickled Python functions and their arguments) to available worker nodes, and each worker node
# executes the task and returns the result to the client.

# Requirements:
# Implement a protocol for serializing and deserializing tasks using pickling.
# Handle task distribution, execution, and result retrieval in both the client and worker nodes.
# Ensure fault tolerance and scalability by handling connection errors, timeouts, and dynamic addition/removal
# of worker nodes.

import socket, pickle
from processdata import ProcessData

HOST = 'localhost'
PORT = 50007
# Create a socket connection.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Create an instance of ProcessData() to send to server.
variable = ProcessData()
# Pickle the object and send it to the server
data_string = pickle.dumps(variable)
s.send(data_string)

s.close()
print ('Data Sent to Server')
