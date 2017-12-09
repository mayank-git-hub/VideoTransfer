#Run this first on the computer where you want to recieve the video


from socket import *
import cv2
import numpy as np

host = "192.168.0.103"	#Here goes the IP address of the computer where you want to send the video to

port = 13000
buf = 184650
addr = (host,port)


UDPSock = socket(AF_INET,SOCK_DGRAM)
UDPSock.bind(addr)
no_packet = 50


host_send = "192.168.0.101"	# Here goes the IP address of the computer which has a camera

port_send = 13001
addr_send = (host_send, port_send)
UDPSock_send = socket(AF_INET, SOCK_DGRAM)



i_ = np.uint8(1).tostring()

while 1:
    frame = np.zeros(921600).astype(np.uint8)

    for i in range(no_packet):
        data,addr = UDPSock.recvfrom(buf)
        frame[i*frame.shape[0]//no_packet:(i+1)*frame.shape[0]//no_packet] = np.fromstring(data, dtype = np.uint8)

    cv2.imshow('frame', np.reshape(frame, (480, 640, 3)))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    UDPSock.sendto(i_, addr_send)

UDPSock.close()
