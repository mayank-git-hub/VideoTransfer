# Run this first on the computer where you want to recieve the video

from socket import *
import cv2
import numpy as np
import config
from PIL import Image
import io

buf = 184650
addr = (config.receiver_ip, config.receiver_port)

UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)

addr_send = (config.sender_ip, config.sender_port)
UDPSock_send = socket(AF_INET, SOCK_DGRAM)

i_ = np.uint8(1).tostring()


while True:

    data, addr = UDPSock.recvfrom(buf)

    length = int(data)
    UDPSock.sendto(i_, addr_send)

    current_image = b''
    frame = np.zeros(921600).astype(np.uint8)

    while len(current_image) != length:
        
        data, addr = UDPSock.recvfrom(buf)
        current_image += data

    frame = np.array(Image.open(io.BytesIO(current_image)))

    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
    # For acknowledgement, otherwise UDP will keep on sending data and that will overlap the buffer
    UDPSock.sendto(i_, addr_send)

UDPSock.close()
