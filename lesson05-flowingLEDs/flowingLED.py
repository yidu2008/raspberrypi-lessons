
import RPi.GPIO as GPIO
import time

pins = [11, 12, 13]

def setup():
    GPIO.setmode(GPIO.BOARD)
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

def loop():
    while True:
        GPIO.output(11, GPIO.LOW)
        time.sleep(5)
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
        time.sleep(6)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
        time.sleep(1.5)
        GPIO.output(12, GPIO.HIGH)

def destroy():
    for pin in pins:
        GPIO.output(pin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()