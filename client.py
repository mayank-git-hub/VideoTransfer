# Run this after running the server.py program on the computer having the camera

from socket import *
import cv2
import config


addr = (config.receiver_ip, config.receiver_port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
no_packet = 50

buf = 50
addr_recv = (config.sender_ip, config.sender_port)
UDPSock_recv = socket(AF_INET, SOCK_DGRAM)
UDPSock_recv.bind(addr_recv)

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    r = frame.reshape(480*640*3)

    for i in range(no_packet):
        UDPSock.sendto(r[i*r.shape[0]//no_packet:(i+1)*r.shape[0]//no_packet].tostring(), addr)

    ack, add = UDPSock_recv.recvfrom(buf)
