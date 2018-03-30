
import RPi.GPIO as GPIO 
import time
from multiprocessing import Process

pins = [11, 19]

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(19, GPIO.HIGH)

def greenlightloop():
    while True:
        print '...led on'
        GPIO.output(19, GPIO.LOW)
        time.sleep(10.0)
        print 'led off...'
        GPIO.output(19, GPIO.HIGH)
        time.sleep(18.0)
        

def loop():
    while True:
        print 'led off...' 
        GPIO.output(11, GPIO.HIGH)
        time.sleep(10.0)
        print '...led on'
        GPIO.output(11, GPIO.LOW)
        time.sleep(0.5)
        print 'led off...'
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.5)
        print '...led on'
        GPIO.output(11, GPIO.LOW)
        time.sleep(0.5)
        print 'led off...'
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.5)
        print '...led on'
        GPIO.output(11, GPIO.LOW)
        time.sleep(0.5)
        print 'led off...'
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.5)
        print '...led on'
        GPIO.output(11, GPIO.LOW)
        time.sleep(0.5)
        print 'led off...'
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.5)
        print '...led on'
        GPIO.output(11, GPIO.LOW)
        time.sleep(0.5)
        print 'led off...'
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.5)
        print '...led on'
        GPIO.output(11, GPIO.LOW)
        time.sleep(0.5)
        print 'led off...'
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.5)
        print '...led on'
        GPIO.output(11, GPIO.LOW)
        time.sleep(0.5)
        print 'led off...'
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.5)
        print '...led on'
        GPIO.output(11, GPIO.LOW)
        time.sleep(0.5)
        print 'led off...'
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.5)
        print '...led on'
        GPIO.output(11, GPIO.LOW)
        time.sleep(10.0)

def destroy():
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(19, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        #loop()
        #greenlightloop()
        p1 = Process(target=loop)
        p1.start()

        p2 = Process(target=greenlightloop)
        p2.start()
    except KeyboardInterrupt: 
        destroy()