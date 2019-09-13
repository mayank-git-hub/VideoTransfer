# Run this first on the computer where you want to recieve the video

from socket import *
import cv2
import numpy as np
import config

buf = 184650
addr = (config.receiver_ip, config.receiver_port)

UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
no_packet = 50

addr_send = (config.sender_ip, config.sender_port)
UDPSock_send = socket(AF_INET, SOCK_DGRAM)

i_ = np.uint8(1).tostring()

while True:
    
    frame = np.zeros(921600).astype(np.uint8)

    for i in range(no_packet):
        
        data, addr = UDPSock.recvfrom(buf)
        frame[i*frame.shape[0]//no_packet:(i+1)*frame.shape[0]//no_packet] = np.fromstring(data, dtype=np.uint8)

    cv2.imshow('frame', np.reshape(frame, (480, 640, 3)))
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
    # For acknowledgement, otherwise UDP will keep on sending data and that will overlap the buffer
    UDPSock.sendto(i_, addr_send)

UDPSock.close()
