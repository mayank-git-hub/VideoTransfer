from socket import *
import cv2
import numpy as np

host = "192.168.0.103"	# Here goes the IP address of the computer you want to send the video to

port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
no_packet = 50


host_recv = "192.168.0.101"	# Here goes the IP address of the computer having the video
port_recv = 13001
buf = 50
addr_recv = (host_recv, port_recv)
UDPSock_recv = socket(AF_INET, SOCK_DGRAM)
UDPSock_recv.bind(addr_recv)

cap = cv2.VideoCapture(0)
while True:
	
    ret, frame = cap.read()
    r = frame.reshape(480*640*3)
    #print(r.shape)
    
    for i in range(no_packet):
        UDPSock.sendto(r[i*r.shape[0]//no_packet:(i+1)*r.shape[0]//no_packet].tostring(), addr)#str.encode(str(
    ack, add = UDPSock_recv.recvfrom(buf)

UDPSock.close()
