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

    udp_sock = socket(AF_INET, SOCK_DGRAM)
    udp_sock.bind(addr)

    addr_send = (config.sender_ip, config.sender_port)

    i_ = np.uint8(1).tostring()

    while True:

        data, addr = udp_sock.recvfrom(buf)

        length = int(data)
        udp_sock.sendto(i_, addr_send)

        current_image = b''

        while len(current_image) != length:

            data, addr = udp_sock.recvfrom(buf)
            current_image += data

        frame = np.array(Image.open(io.BytesIO(current_image)))

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # For acknowledgement, otherwise UDP will keep on sending data and that will overlap the buffer
        udp_sock.sendto(i_, addr_send)

    udp_sock.close()
