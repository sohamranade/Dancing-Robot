from lx16a import *
from math import sin, cos
import time

# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc...
# On Raspbian, try each port in /dev/
LX16A.initialize("COM9")

# There should two servos connected, with IDs 1 and 2
servo1 = LX16A(1)
servo2 = LX16A(2)

t = 0

flag = True

while flag:
	# Two sine waves out of phase
	# The servos can rotate between 0 and 240 degrees,
	# So we adjust the waves to be in that range
	#servo1.moveTimeWrite(sin(t) * 120 + 120)
	servo1.moveTimeWriteRel(60, time = 2000)
	servo1.angleOffsetWrite()
	servo2.moveTimeWriteRel(60, time = 2000)
	servo2.angleOffsetWrite()

	time.sleep(3)
	servo1.moveTimeWriteRel(-60, time = 2000)
	servo1.angleOffsetWrite()
	servo2.moveTimeWriteRel(-60, time = 2000)
	servo2.angleOffsetWrite()

	t += 0.01
	flag = False