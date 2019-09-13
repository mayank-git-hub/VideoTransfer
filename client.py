# Run this after running the server.py program on the computer having the camera

from socket import *
import cv2
import config
import io
from PIL import Image


addr = (config.receiver_ip, config.receiver_port)
UDPSock = socket(AF_INET, SOCK_DGRAM)

buf = 50
addr_recv = (config.sender_ip, config.sender_port)
UDPSock_recv = socket(AF_INET, SOCK_DGRAM)
UDPSock_recv.bind(addr_recv)

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    # Converting image to JPEG format to save bandwidth

    pil_frame = Image.fromarray(frame)
    tmpFile = io.BytesIO()
    pil_frame.save(tmpFile, format="jpeg")
    png_buffer = tmpFile.getvalue()

    UDPSock.sendto(str(len(png_buffer)).encode(), addr)
    UDPSock_recv.recvfrom(buf)

    UDPSock.sendto(png_buffer, addr)
    UDPSock_recv.recvfrom(buf)
