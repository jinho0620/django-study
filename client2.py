import urllib.request

fhand = urllib.request.urlopen("http://localhost:9000/something")

for line in fhand:
    print(line.decode().strip())