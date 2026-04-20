import socket

HOST = "0.0.0.0"
PORT = 5001

server = socket.socket()
server.bind((HOST,PORT))
server.listen(1)

print("Waiting for connection...")
conn, addr = server.accept()
print(f"Connected from {addr}")
command = conn.recv(1024).decode()
print("Command:",command)
match command:
    case "1":
        message = conn.recv(4096).decode()
        print(message)
    case "2":
        with open("reciever_text.txt","w") as f:
            data = conn.recv(4096).decode()
            f.write(data)
        print("Text file recieved")
    case "3":
        with open("reciever_image.png","wb") as f:
            while True:
                data = conn.recv(4096)
                if not data:
                    break
                f.write(data)
        print("Got the image")
    case "4":
        with open("reciever_audio.mp3","wb") as f:
            while True:
                data = conn.recv(4096)
                if not data:
                    break
                f.write(data)
        print("Got the image")
    case "5":
        with open("reciever_video.mp4","wb") as f:
            while True:
                data = conn.recv(4096)
                if not data:
                    break
                f.write(data)
        print("Got the image")
