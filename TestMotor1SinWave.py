from lx16a import *
from math import sin, cos
import time

# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc...
# On Raspbian, try each port in /dev/
try:
	LX16A.initialize("COM9")

	# There should two servos connected, with IDs 1 and 2
	servo1 = LX16A(7)

	t = 0

	flag = True

	time.sleep(1)

	print("Motor id is ", servo1.IDRead())
	print("Angle offset is ", servo1.angleOffsetRead())
	print("Angle limit is ", servo1.angleLimitRead())
	print("Physical pos is ", servo1.getPhysicalPos());
	print("Virtual pos is ", servo1.getVirtualPos());
	print("Current temperature is ", servo1.tempRead())
	print("Current voltage is ", servo1.vInRead())
except KeyboardInterrupt:
	quit()


# while (t < .5):
# 	# Two sine waves out of phase
# 	# The servos can rotate between 0 and 240 degrees,
# 	# So we adjust the waves to be in that range

# 	servo1.moveTimeWrite(sin(10*t) * 120)
# 	print("Motor id is ", servo1.IDRead())
# 	print("Angle offset is ", servo1.angleOffsetRead())
# 	print("Angle limit is ", servo1.angleLimitRead())
# 	print("Physical pos is ", servo1.getPhysicalPos());
# 	print("Virtual pos is ", servo1.getVirtualPos());
# 	print("Current temperature is ", servo1.tempRead())
# 	print("Current voltage is ", servo1.vInRead())
# 	t += 0.005
# 	flag = False

# try:
# 	while True:
# 		servo1.motorMode(600)
# 		time.sleep(5)
# 		# servo1.motorMode(-1000)
# 		# time.sleep(5)
# except KeyboardInterrupt:
# 	servo1.servoMode()