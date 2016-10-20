import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

map = {'d1' : 18, 'a' : 17, 'f' : 27, 'd2' : 22, 'd3' : 23, 'b' : 24, 'e' : 26, 'd' : 19, 'c' : 13, 'g' : 6, 'd4' : 5}
d1=18
a=17
f=27
d2=22
d3=23
b=24
e=26
d=19
c=13
g=6
d4=5

def up(pin):
	GPIO.output(pin,GPIO.HIGH)
def down(pin):
	GPIO.output(pin,GPIO.LOW)


def clear():
	for pin in [18, 17, 27, 22, 23, 24, 26, 19, 13, 6, 5]:
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, GPIO.LOW)
clear()
def downall():
	down(a)
	down(b)
	down(c)
	down(d)
	down(e)
	down(f)
	down(g)

def upall():
	up(a)
	up(b)
	up(c)
	up(d)
	up(e)
	up(f)
	up(g)
	
def zero():
	downall()
	up(g)

def one():
	upall()
	down(b)
	down(c)
def two():
	downall()
	up(f)
	up(c)
def three():
	downall()
	up(f)
	up(e)
def four():
	downall()
	up(a)
	up(e)
	up(d)
def five():
	downall()
	up(b)
	up(e)
def six():
	downall()
	up(b)
def seven():
	upall()
	down(a)
	down(b)
	down(c)
def eight():
	downall()
def nine():
	downall()
	up(e)
def downdigits():
	down(d1)
	down(d2)
	down(d3)
	down(d4)

def digit(id, num):
	if id == 1:
		digit = d1
	elif id == 2:
		digit = d2
	elif id == 3:
		digit = d3
	elif id == 4:
		digit = d4
	
	down(digit)
	if num == 1:
		one()
	elif num == 2:
		two()
	elif num == 3:
		three()
	elif num == 4:
		four()
	elif num == 5:
		five()
	elif num == 6:
		six()
	elif num == 7:
		seven()
	elif num == 8:
		eight()
	elif num == 9:
		nine()
	elif num == 0:
		zero()
	up(digit)	
import random
import datetime
#for i in range(0, 10):
pins = [4, 3, 2, 1]
display = [1, 2, 4, 5]
while True:
	now = time.strftime("%I:%M")
	#now = time.strftime("%H:%M")
	now = now.split(":")
	hour = str(now[0])
	minute = str(now[1])
	display[0] = int(hour[0])
	display[1] = int(hour[1])
	display[2] = int(minute[0])
	display[3] = int(minute[1])
	
	for pin in pins:
		downdigits()
		#digit(pin, random.randint(0, 9))
		digit(pin, display[pin-1])
		time.sleep(0.002)

#digit(4, 2)

#digit(3, 0)
#digit(1, 1)

exit(0)
while True:
	pin = raw_input("CMD> ")
	pin = pin.split(" ")
	if pin[1] == "on":
		up(map[pin[0]])
	else:
		down(map[pin[0]])
	#clear()
	
