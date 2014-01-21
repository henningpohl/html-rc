import time
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def tryMusic():
    sock.sendto("playSong test.mp3", ("localhost", 43000))
    time.sleep(10.0)
    sock.sendto("pauseMusic", ("localhost", 43000))

def tryColor():
    sock.sendto("setBackgroundColor 0 0 0 255 1", ("localhost", 43000))
    sock.sendto("setGlow 0.0 0 0 0 255 1", ("localhost", 43000))
    time.sleep(1.0)
    sock.sendto("setBackgroundColor 55 55 55 255 3000", ("localhost", 43000))
    sock.sendto("setGlow 0.85 200 200 200 255 1000", ("localhost", 43000))
    time.sleep(3.0)
    sock.sendto("setGlow 0.5 255 100 100 255 3000", ("localhost", 43000))
    sock.sendto("setBackgroundColor 0 0 0 255 590", ("localhost", 43000))

def tryVideo():
    sock.sendto("playYoutubeVideo kpAaVA3WWt0 33", ("localhost", 43000))
    

#tryMusic()
#tryColor()
#tryVideo()
