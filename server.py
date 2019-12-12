# Run this first on the computer where you want to receive the video

from socket import *
import cv2
import numpy as np
import config
from PIL import Image
import io


def server():

    buf = 184650
    addr = (config.receiver_ip, config.receiver_port)

    tcp_sock = socket(AF_INET, SOCK_STREAM)
    tcp_sock.bind(addr)

    addr_send = (config.sender_ip, config.sender_port)

    i_ = np.uint8(1).tostring()

    tcp_sock.listen(1)
    c, addr_sender = tcp_sock.accept() 

    no = 0
    while True:
        no += 1
        data = c.recv(buf)

        length = int(data)
        c.send(i_)

        current_image = b''

        while len(current_image) != length:

            data = c.recv(buf)
            current_image += data

        frame = np.array(Image.open(io.BytesIO(current_image)))

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # For acknowledgement, otherwise UDP will keep on sending data and that will overlap the buffer
        c.send(i_)

    c.close()
