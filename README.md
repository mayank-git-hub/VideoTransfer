# VideoTransfer
Transfer video from one device having camera to another.

So motivated by not having to buy a new camera for my pc I tried to apply socket programming for transferring my laptop's video to my PC. 
<br>It was a fun thing to do and has a lot of application for setting up a server which can control other robots which don't have enough<br>
computation power to do it on their own.

It was done in python as it is user friendly for images.


# To install the requirements using pip - 
    pip install -r requirements.txt
    
# To run the client program - 

    python main.py client
    
# To run the server program - 

    python main.py server
    
## Notes

The file client.py should be run on the system having the camera and the server should be run where you want the video to be sent.
There is currently a bug now which will be fixed as soon as possible, but it is a small bug. The bug is that you must run the server code before running the client code. At least this bug is present when the client code is run in windows and the server on ubuntu.

Don't forget to change the IP address in the config.py
