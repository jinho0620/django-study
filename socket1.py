import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True: # Loop is necessary since how much data we will get from the server
    data = mysock.recv(512) # Read up to 512 bytes from the buffered data
    if len(data) < 1: # If no data is coming in, stop reading
        break
    print(data.decode(), end="")

mysock.close()