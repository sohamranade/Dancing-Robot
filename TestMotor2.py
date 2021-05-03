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
	print("Motor id is ", servo1.IDRead())
	print("Angle offset is ", servo1.angleOffsetRead())
	print("Angle limit is ", servo1.angleLimitRead())
	print("Physical pos is ", servo1.getPhysicalPos());
	print("Virtual pos is ", servo1.getVirtualPos());
	print("Current temperature is ", servo1.tempRead())
	print("Current voltage is ", servo1.vInRead())
	servo1.moveTimeWriteRel(30, time = 1000)
	servo1.angleOffsetWrite()
	print("Angle offset is ", servo1.angleOffsetRead())
	print("Physical pos is ", servo1.getPhysicalPos());
	print("Virtual pos is ", servo1.getVirtualPos());
	print("Current temperature is ", servo1.tempRead())
	print("Current voltage is ", servo1.vInRead())
	time.sleep(2)
	servo1.moveTimeWriteRel(-30, time = 1000)
	servo1.angleOffsetWrite()
	print("Angle offset is ", servo1.angleOffsetRead())
	print("Physical pos is ", servo1.getPhysicalPos());
	print("Virtual pos is ", servo1.getVirtualPos());
	print("Current temperature is ", servo1.tempRead())
	print("Current voltage is ", servo1.vInRead())

	time.sleep(2)
	print("Motor id is ", servo2.IDRead())
	print("Angle offset is ", servo2.angleOffsetRead())
	print("Angle limit is ", servo2.angleLimitRead())
	print("Physical pos is ", servo2.getPhysicalPos());
	print("Virtual pos is ", servo2.getVirtualPos());
	print("Current temperature is ", servo2.tempRead())
	print("Current voltage is ", servo2.vInRead())
	servo2.moveTimeWriteRel(30, time = 1000)
	servo2.angleOffsetWrite()
	print("Angle offset is ", servo2.angleOffsetRead())
	print("Physical pos is ", servo2.getPhysicalPos());
	print("Virtual pos is ", servo2.getVirtualPos());
	print("Current temperature is ", servo2.tempRead())
	print("Current voltage is ", servo2.vInRead())
	time.sleep(2)
	servo2.moveTimeWriteRel(-30, time = 1000)
	servo2.angleOffsetWrite()
	print("Angle offset is ", servo2.angleOffsetRead())
	print("Physical pos is ", servo2.getPhysicalPos());
	print("Virtual pos is ", servo2.getVirtualPos());
	print("Current temperature is ", servo2.tempRead())
	print("Current voltage is ", servo2.vInRead())
	t += 0.01
	flag = False