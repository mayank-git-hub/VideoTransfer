# Run this after running the server.py program on the computer having the camera

from socket import *
import cv2
import config
import io
from PIL import Image


def client():

    addr = (config.receiver_ip, config.receiver_port)
    udp_sock = socket(AF_INET, SOCK_DGRAM)

    buf = 50
    addr_recv = (config.sender_ip, config.sender_port)
    udp_sock_recv = socket(AF_INET, SOCK_DGRAM)
    udp_sock_recv.bind(addr_recv)

    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        # Converting image to JPEG format to save bandwidth

        pil_frame = Image.fromarray(frame)
        tmp_file = io.BytesIO()
        pil_frame.save(tmp_file, format="jpeg")
        png_buffer = tmp_file.getvalue()

        udp_sock.sendto(str(len(png_buffer)).encode(), addr)
        udp_sock_recv.recvfrom(buf)

        udp_sock.sendto(png_buffer, addr)
        udp_sock_recv.recvfrom(buf)
