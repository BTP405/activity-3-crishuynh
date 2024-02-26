import socket, pickle

print ("Server is Listening.....")
HOST = 'localhost'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ('Connected by'), addr

data = conn.recv(4096)
data_variable = pickle.loads(data)
conn.close()
print (data_variable)
print ('Data received from client')
