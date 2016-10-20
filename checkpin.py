import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(6,GPIO.IN, pull_up_down=GPIO.PUD_UP)

initial_state = 0
while True:
	input_state = GPIO.input(6)
	if input_state == False and initial_state == 0:
    		print("Ring bell!!!!")
		initial_state = 1
		time.sleep(0.2)
		
	elif input_state == True and initial_state == 1:
		initial_state = 0;
    
