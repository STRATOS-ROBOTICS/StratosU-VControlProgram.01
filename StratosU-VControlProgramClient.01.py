import pygame
from pygame.locals import *
import cv2
import numpy as np
import sys
import socket

camera = cv2.VideoCapture("udp://@192.168.1.58:5000?overrun_nonfatal=1&fifo_size=5000000")
pygame.init()
pygame.display.set_caption("OpenCV camera stream on Pygame")
screen = pygame.display.set_mode([640,480])
SERVER = "192.168.1.58"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
client.sendall(bytes("This is from Client",'UTF-8'))

try:
    while True:

        ret, frame = camera.read()
		
        screen.fill([0,0,0])
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = pygame.surfarray.make_surface(frame)
        screen.blit(frame, (0,0))
        pygame.display.update()

        for event in pygame.event.get():
           if event.type == KEYDOWN and event.key == K_a:
                print ("ok")
           elif event.type == KEYDOWN and event.key == K_l:
                in_data =  client.recv(2048)
                print("From Server :" ,in_data.decode())
                out_data = ("start")
                client.sendall(bytes(out_data,'UTF-8'))
           elif event.type == KEYDOWN and event.key == K_p:
                in_data =  client.recv(2048)
                print("From Server :" ,in_data.decode())
                out_data = ("stop")
                client.sendall(bytes(out_data,'UTF-8'))
           elif event.type == KEYDOWN and event.key == K_s:
                sys.exit(0)
except (KeyboardInterrupt,SystemExit):
    pygame.quit()
    cv2.destroyAllWindows()





