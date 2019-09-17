# StratosU-VControlProgram.01
StratosU-VControlProgram.01

Control one adafruit DC motor (4 DC motors can be use and have camera view of a raspicam in real time IN pygame display over wifi or cable.
pygame+opencv+adafruit+raspberry = a perfect combo for  robots or Unnmaned.Vehicles with A.I image filterings, 100m range can be better range with wifi repetiter...) very good battery autonomous, lightweight affordable...




STEPS
-----

01-start the server on the raspberry

02-start the client on the desktop

03-open a new terminal in raspberry and launch this comand : raspivid -t 0 -b 2000000 -fps 30 -w 640 -h 480 -o - -rot 180 | nc -p 1904 -u 192.168.1.62 5000       

ENJOY

STRATOS 2019
