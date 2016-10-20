
#read.py
from evdev import InputDevice, categorize, ecodes


#mapping event codes to numbers
map = (0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
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

dev = InputDevice('/dev/input/event0')

while True:
	string = ""
	for event in dev.read_loop():
		if event.code == 28:
			break
		if event.code > 1 and event.code < 12 and event.value == 0:
			string += str(map[event.code])
	if string != "":
		print string


