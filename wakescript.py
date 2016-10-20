
import os
import datetime
import time
while True:
	now = time.strftime("%I:%M")
	if now == "07:00":
		os.system("python wake.py")
		break
