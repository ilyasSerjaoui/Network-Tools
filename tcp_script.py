import socket

target_host = "www.google.com"
target_port = 80

# Create a Socket Object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect The Client
client.connect((target_host,target_port))

# Send Some Data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive Some Data
response = client.recv(4096)

print(response.decode("utf-8", errors="ignore"))
