import socket

HOST = "Address"
PORT = 5001

client = socket.socket()
client.connect((HOST,PORT))
with open("image.png", "rb") as f:
    while True:
        data = f.read(4096)
        if not data:
            break
        client.sendall(data)
print("Image sent")
client.close()