from lx16a import *
from math import sin, cos, pi
import time

# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc...
# On Raspbian, try each port in /dev/
try:
	LX16A.initialize("COM9")

	# There should two servos connected, with IDs 1 and 2
	servo1 = LX16A(7)
	servo2 = LX16A(8)

	t = 0

	flag2Move = False

	servo1.servoMode()
	servo2.servoMode()

	print("Motor id is ", servo1.IDRead())
	print("Angle offset is ", servo1.angleOffsetRead())
	print("Angle limit is ", servo1.angleLimitRead())
	print("Physical pos is ", servo1.getPhysicalPos())
	print("Virtual pos is ", servo1.getVirtualPos())
	print("Current temperature is ", servo1.tempRead())
	print("Current voltage is ", servo1.vInRead())

	print("Motor id is ", servo2.IDRead())
	print("Angle offset is ", servo2.angleOffsetRead())
	print("Angle limit is ", servo2.angleLimitRead())
	print("Physical pos is ", servo2.getPhysicalPos())
	print("Virtual pos is ", servo2.getVirtualPos())
	print("Current temperature is ", servo2.tempRead())
	print("Current voltage is ", servo2.vInRead())

	t = 0;
	print("Starting initialization")
	while (sin(10*t*2*pi/360)*120 < 120):
		print("Motor id is ", servo1.IDRead())
		print("Physical pos is ", servo1.getPhysicalPos())
		print("Virtual pos is ", servo1.getVirtualPos())
		print("Motor id is ", servo2.IDRead())
		print("Physical pos is ", servo2.getPhysicalPos())
		print("Virtual pos is ", servo2.getVirtualPos())
		servo1.moveTimeWrite(sin(10*t*2*pi/360)*120)
		servo2.moveTimeWrite(sin(10*t*2*pi/360)*120)
		t+=1
	print("End initialization")

	time.sleep(2)


	print("Motor id is ", servo1.IDRead())
	print("Angle offset is ", servo1.angleOffsetRead())
	print("Angle limit is ", servo1.angleLimitRead())
	print("Physical pos is ", servo1.getPhysicalPos())
	print("Virtual pos is ", servo1.getVirtualPos())
	print("Current temperature is ", servo1.tempRead())
	print("Current voltage is ", servo1.vInRead())

	print("Motor id is ", servo2.IDRead())
	print("Angle offset is ", servo2.angleOffsetRead())
	print("Angle limit is ", servo2.angleLimitRead())
	print("Physical pos is ", servo2.getPhysicalPos())
	print("Virtual pos is ", servo2.getVirtualPos())
	print("Current temperature is ", servo2.tempRead())
	print("Current voltage is ", servo2.vInRead())

	#initial position
	if abs(servo1.getPhysicalPos() - 120) > 20:
		raise Exception("Initial position is not 120")

	if (abs(servo2.getPhysicalPos() - 120) > 20):
		raise Exception("Initial position is not 120")

	t = 0;
	while (t < 5):
		print("Motor id is ", servo1.IDRead())
		print("Physical pos is ", servo1.getPhysicalPos())
		print("Virtual pos is ", servo1.getVirtualPos())
		print("Current temperature is ", servo1.tempRead())
		print("Current voltage is ", servo1.vInRead())

		print("Motor id is ", servo2.IDRead())
		print("Physical pos is ", servo2.getPhysicalPos())
		print("Virtual pos is ", servo2.getVirtualPos())
		print("Current temperature is ", servo2.tempRead())
		print("Current voltage is ", servo2.vInRead())
		servo1.motorMode(1000)
		servo2.motorMode(1000)
		time.sleep(.01)
		t+=.1;

	servo1.moveStop();
	servo2.moveStop();
	time.sleep(2);
	servo1.servoMode()
	servo2.servoMode()

	t = 0;
	while (sin(10*t*2*pi/360)*120 < 120):
		servo1.moveTimeWrite(sin(10*t*2*pi/360)*120)
		servo2.moveTimeWrite(sin(10*t*2*pi/360)*120)
		t+=1

	time.sleep(2)

	print("Motor id is ", servo1.IDRead())
	print("Angle offset is ", servo1.angleOffsetRead())
	print("Angle limit is ", servo1.angleLimitRead())
	print("Physical pos is ", servo1.getPhysicalPos())
	print("Virtual pos is ", servo1.getVirtualPos())
	print("Current temperature is ", servo1.tempRead())
	print("Current voltage is ", servo1.vInRead())

	print("Motor id is ", servo2.IDRead())
	print("Angle offset is ", servo2.angleOffsetRead())
	print("Angle limit is ", servo2.angleLimitRead())
	print("Physical pos is ", servo2.getPhysicalPos())
	print("Virtual pos is ", servo2.getVirtualPos())
	print("Current temperature is ", servo2.tempRead())
	print("Current voltage is ", servo2.vInRead())

	#final position before shutdown
	if (abs(servo1.getPhysicalPos() - 120) > 20):
		raise Exception("Initial position is not 120")
	if (abs(servo2.getPhysicalPos() - 120) > 20):
		raise Exception("Initial position is not 120")

except KeyboardInterrupt:
	servo1.servoMode()
	servo2.servoMode()
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