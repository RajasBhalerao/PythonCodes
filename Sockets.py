import socket
#The below two lines just "dials the number" no data is transfered yet. This is the transport layer
#Sock_Stream is a connection point in your system which is not yet connected to the far end.
#AF_INET is for hooking the connection
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org',80))
#preparing to send the request
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
#actually send the request
mysocket.send(cmd)

while True:
    #Reciveing upto 512 chars
    data = mysocket.recv(512)
    if (len(data)<1):
        break
    print((data.decode()))
#Always close the socket because it takes up resources to run on both sides.
mysocket.close()
