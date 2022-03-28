import socket

webhost = "localhost"
port = 8080

print(f"Connecting to {webhost} on {port}")
webclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
webclient.connect((webhost, port))
webclient.send(bytes("GET / HTTP/1.1\r\nHost: localhost\r\n\r\n".encode("utf-8")))
reply = webclient.recv(4096)
print(f"Response received from {webhost}")
print(reply.decode())
