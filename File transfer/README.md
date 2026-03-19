# Image Transfer App (Python)

## Summary
A simple Python application that transfers images between devices on the same local network using sockets.

## How It Works
- One device runs the **receiver (server)** to listen for incoming files.
- Another device runs the **sender (client)** to send an image.
- The image is transferred over the local network using the device's IP address and a specified port both have to be on the same network.

## Requirements
- Python 3.x
- Both devices must be connected to the same network (WiFi or LAN)

## Setup

### Find the Receiver's IP Address
On the receiving computer, run:
```bash
ipconfig
```
Change the HOST (in the sender.py) to the IPv4 address of the receiver.
1. Make sure the image file name matches the name used in the code.
2. By default, `sender.py` looks for a file named `image.png` in the same folder as the script. If your image has a different name, either rename the file to `image.png` or update the code to use your image's file name.
3. Start the receiver first by running `reciever.py`.
4. After the receiver is waiting for a connection, run `sender.py`.
