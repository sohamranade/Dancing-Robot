from lx16a import *
from math import sin, cos, pi
import time
import xlwt
import pandas as pd
import numpy as np
from xlwt import Workbook

def initializeMotor(servo1):
	targetPos = 120;
	initialPos = servo1.getPhysicalPos();
	error = targetPos-initialPos

	print(servo1.IDRead())
	print(initialPos)
	print(error)

	t=0;
	while (abs(sin(t*2*pi/360)*error) < abs(error)):
		# print("Motor id is ", servo1.IDRead())
		# print("Physical pos is ", servo1.getPhysicalPos())
		# print("Virtual pos is ", servo1.getVirtualPos())
		servo1.moveTimeWrite(sin(t*2*pi/360)*error+initialPos)
		time.sleep(.01)
		t+=3

def resetAllMotors(servoL1, servoL2, servoA1S, servoA1E, servoA2S, servoA2E):
	initializeMotor(servoL1);
	initializeMotor(servoL2);
	initializeMotor(servoA1S);
	initializeMotor(servoA1E);
	initializeMotor(servoA2S);
	initializeMotor(servoA2E);

# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc...
# On Raspbian, try each port in /dev/
try:
	
	LX16A.initialize("COM9")

	servoL1 = LX16A(7)
	servoL2 = LX16A(8)
	servoA1S = LX16A(2)
	servoA1E = LX16A(1)
	servoA2S = LX16A(4)
	servoA2E = LX16A(3)


	t = 0

	flag2Move = False

	servoL1.servoMode()
	servoL2.servoMode()
	servoA1S.servoMode()
	servoA1E.servoMode()
	servoA2S.servoMode()
	servoA2E.servoMode()

	print("Starting initialization")
	resetAllMotors(servoL1, servoL2, servoA1S, servoA1E, servoA2S, servoA2E)
	print("End initialization")
	

except KeyboardInterrupt:
	quit()
