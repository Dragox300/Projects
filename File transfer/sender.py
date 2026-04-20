import socket

HOST = "Address"
PORT = 5001
print(f"""Enter the number of one of the following options
            1) Simple message
            2) Text file
            3) Image
            4) Audio
            5) Video""")
command = input()
match command:
    case "1":
        client = socket.socket()
        client.connect((HOST,PORT))
        client.sendall(command.encode())
        message = input("What is the message\n")
        client.sendall(message.encode())
        client.close()
    case "2":
        client = socket.socket()
        client.connect((HOST,PORT))
        client.sendall(command.encode())
        with open("text.txt", "r") as f:
            data = f.read()
            client.sendall(data.encode())
        print("Text sent")
        client.close()
    case "3":
        client = socket.socket()
        client.connect((HOST,PORT))
        client.sendall(command.encode())
        with open("image.png", "rb") as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                client.sendall(data)
        print("Image sent")
        client.close()
    case "4":
        client = socket.socket()
        client.connect((HOST,PORT))
        client.sendall(command.encode())
        with open("audio.mp3", "rb") as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                client.sendall(data)
        print("Audio sent")
        client.close()
    case "5":
        client = socket.socket()
        client.connect((HOST,PORT))
        client.sendall(command.encode())
        with open("video.mp4", "rb") as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                client.sendall(data)
        print("Video sent")
        client.close()
