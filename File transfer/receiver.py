import socket

HOST = "0.0.0.0"
PORT = 5001

server = socket.socket()
server.bind((HOST, PORT))
server.listen(1)

print("Waiting for connection...")
conn, addr = server.accept()
print(f"Connected from {addr}")

with open("received_image.png", "wb") as f:
    while True:
        data = conn.recv(4096)
        if not data:
            break
        f.write(data)

print("Image received!")
conn.close()