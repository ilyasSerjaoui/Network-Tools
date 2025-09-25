import socket

target_host = "127.0.0.1"
target_port = 80

# Create a Socket Object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send Some Data
client.sendto(b"AAABBBCCC",(target_host, target_port))

# Receive Some Data
data, addr = client.recvfrom(4096)

print(data)
