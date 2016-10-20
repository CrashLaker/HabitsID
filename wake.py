import RPi.GPIO as GPIO
from time import sleep

# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 
pin = 18
# Set relay pins as output
GPIO.setup(pin, GPIO.OUT)

delay = 0.1
delay2=2
for i in range(0, 10): 
# Turn all relays ON
	GPIO.output(pin, GPIO.HIGH)
# Sleep for 5 seconds
	sleep(delay) 
# Turn all relays OFF
	GPIO.output(pin, GPIO.LOW)
# Sleep for 5 seconds
	sleep(delay2)
