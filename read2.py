
#read.py
from evdev import InputDevice, categorize, ecodes
from select import select
import os

os.system("rm /var/www/html/habits/entry.txt")
os.system("touch /var/www/html/habits/entry.txt")

def auth(string, id):
	dict = {'0005191107' : 'yellow', '0007285251' : 'green', '0005195908' : 'blue', '0005190921' : 'pink'}
	if not string in dict:
		return
	#print dict[string]
	finalstring = ""
	print id, " ", string
	side = "left"
	if id == 4:
		side = "right"
	if dict[string] == "yellow":
		if side == "left":
			os.system("python red.py &")
		else:
			os.system("python red2.py &")
			
		finalstring = side + ",dn.png," + dict[string]
	else:
		if side == "left":
			os.system("python green.py &")
		else:
			os.system("python green2.py &")
			
		finalstring = side + ",ok.png," + dict[string]
		os.system("python relay.py &")
	os.system("echo \""+finalstring+"\" >> /var/www/html/habits/entry.txt &")

#mapping event codes to numbers
mapkeyboard = (0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
#Event code 1 (KEY_ESC)
#Event code 2 (KEY_1)
#Event code 3 (KEY_2)
#Event code 4 (KEY_3)
#Event code 5 (KEY_4)
#Event code 6 (KEY_5)
#Event code 7 (KEY_6)
#Event code 8 (KEY_7)
#Event code 9 (KEY_8)
#Event code 10 (KEY_9)
#Event code 11 (KEY_0)

#dev = InputDevice('/dev/input/event0')
devices = map(InputDevice, ('/dev/input/event0', '/dev/input/event1'))
devices = {dev.fd: dev for dev in devices}

#for dev in devices.values(): print(dev)



while True:
	string = ""
	r, w, x = select(devices, [], [])
	for fd in r:
		string = ""
		for event in devices[fd].read_loop():
			if event.code == 28:
				break
			if event.code > 1 and event.code < 12 and event.value == 0:
				string += str(mapkeyboard[event.code])
		if string != "":
			auth(string, fd)



