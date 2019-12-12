# Run this after running the server.py program on the computer having the camera

from socket import *
import cv2
import config
import io
from PIL import Image


def client(video):

    addr = (config.receiver_ip, config.receiver_port)
    tcp_sock = socket(AF_INET, SOCK_STREAM)

    buf = 50

    cap = cv2.VideoCapture(video)

    tcp_sock.connect(addr)

    while True:

        ret, frame = cap.read()

        # Converting image to JPEG format to save bandwidth

        pil_frame = Image.fromarray(frame)
        tmp_file = io.BytesIO()
        pil_frame.save(tmp_file, format="jpeg")
        png_buffer = tmp_file.getvalue()

        tcp_sock.send(str(len(png_buffer)).encode())
        tcp_sock.recv(buf)

        tcp_sock.send(png_buffer)
        tcp_sock.recv(buf)
