
from socket import *
from time import time
import RPi.GPIO as GPIO

LedPin = 11

HOST = ''
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.output(LedPin, GPIO.HIGH)

def loop():
    while True:
        print 'Waiting for connection...'
        tcpCliSock, addr = tcpSerSock.accept()
        print '...connected from :', addr
        while True:
            data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        if data == 'ON':
            GPIO.output(LedPin, GPIO.LOW)
            print 'led on'
        elif data == 'OFF':
			GPIO.output(LedPin, GPIO.HIGH)
			print 'led off'
	    else:
			print 'error cmd !'
	tcpSerSock.close()

if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		tcpSerSock.close()
 