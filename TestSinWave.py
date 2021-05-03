from lx16a import *
from math import sin, cos, pi
import time

try:
	LX16A.initialize("COM9")

	# There should two servos connected, with IDs 1 and 2
	servo1 = LX16A(7)
	servo2 = LX16A(8)


	flag2Move = False

	servo1.servoMode()
	servo2.servoMode()

	t = 0;
	print("Starting initialization")
	while (sin(t*2*pi/360)*120 < 120):
		print(sin(t*2*pi/360)*120)
		servo1.moveTimeWrite(sin(t*2*pi/360)*120)
		servo2.moveTimeWrite(sin(t*2*pi/360)*120)
		print("Motor id is ", servo1.IDRead())
		print("Physical pos is ", servo1.getPhysicalPos())
		print("Virtual pos is ", servo1.getVirtualPos())
		print("Motor id is ", servo2.IDRead())
		print("Physical pos is ", servo2.getPhysicalPos())
		print("Virtual pos is ", servo2.getVirtualPos())
		t+=1
	print("End initialization")

except KeyboardInterrupt:
	servo1.servoMode()
	servo2.servoMode()
	quit()