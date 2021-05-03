from lx16a import *
from math import sin, cos, pi
import time
import xlwt
import pandas as pd
import numpy as np
from xlwt import Workbook

class RecordMotorData():
	def __init__ (self, servo):
		self.servo = servo;
		self.id = [];
		self.angleOffset = [];
		self.physicalPos = [];
		self.virtualPos = [];
		self.temp = [];
		self.voltage = [];
	def record(self):
		self.id.append(int(self.servo.IDRead()))
		self.angleOffset.append(int(self.servo.angleOffsetRead()))
		self.physicalPos.append(int(self.servo.getPhysicalPos()))
		self.virtualPos.append(int(self.servo.getVirtualPos()))
		self.temp.append(int(self.servo.tempRead()))
		self.voltage.append(int(self.servo.vInRead()))

def save2CSV(recordMotorDataList):
	id = [];
	angleOffset = [];
	physicalPos = [];
	virtualPos = [];
	temp = [];
	voltage = [];
	for recordMotorData in recordMotorDataList:
		id.extend(recordMotorData.id);
		angleOffset.extend(recordMotorData.angleOffset);
		physicalPos.extend(recordMotorData.physicalPos);
		virtualPos.extend(recordMotorData.virtualPos);
		temp.extend(recordMotorData.temp);
		voltage.extend(recordMotorData.voltage);
	
	df = pd.DataFrame(list(zip(id, angleOffset, physicalPos, virtualPos, temp, voltage)), columns = ["Id", "Angle offset", "Physical pos", "Virtual pos", "Temp", "Voltage"])
	df.to_csv(r'MotorData.csv')

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

def danceLegs1(servo1, servo2,cycles, relativeAngleStep, r1, r2):
	print("Starting dance 1")
	direction = 1;
	for i in range(0,cycles):
		t=0;
		initialPos1 = servo1.getPhysicalPos();
		initialPos2 = servo2.getPhysicalPos();
		while (t<180):
			r1.record();
			r2.record();
			# print(sin(t*2*pi/360)*relativeAngleStep)
			# print("Motor id is ", servo1.IDRead())
			# print("Physical pos is ", servo1.getPhysicalPos())
			# print("Virtual pos is ", servo1.getVirtualPos())
			# print("Motor id is ", servo2.IDRead())
			# print("Physical pos is ", servo2.getPhysicalPos())
			# print("Virtual pos is ", servo2.getVirtualPos())
			servo1.moveTimeWrite(direction*sin(t*3*pi/360)*relativeAngleStep+initialPos1);
			servo2.moveTimeWrite(direction*sin(t*3*pi/360)*relativeAngleStep+initialPos2);
			time.sleep(.01)	
			t+=5;
		direction= -direction;

def turnL1A2(servoLeg1, servoLeg2, servoArm1S, servoArm1E, servoArm2S, servoArm2E, 
	cycles, angleStepLeg, angleStepShoulder, angleStepElbow, r1, r2):
	print("Starting dance legs with arms")
	direction = 1;
	for i in range(0,cycles):
		t=0;

		initialPosL1 = servoLeg1.getPhysicalPos();
		initialPosL2 = servoLeg2.getPhysicalPos();

		initialPosA1S = servoArm1S.getPhysicalPos();
		initialPosA1E = servoArm1E.getPhysicalPos();

		initialPosA2S = servoArm2S.getPhysicalPos();
		initialPosA2E = servoArm2E.getPhysicalPos();

		while (t<180):
			r1.record();
			r2.record();
			# print(sin(t*2*pi/360)*angleStepLeg)
			# print("Motor id is ", servoLeg1.IDRead())
			# print("Physical pos is ", servoLeg1.getPhysicalPos())
			# print("Virtual pos is ", servoLeg1.getVirtualPos())
			# print("Motor id is ", servoLeg2.IDRead())
			# print("Physical pos is ", servoLeg2.getPhysicalPos())
			# print("Virtual pos is ", servoLeg2.getVirtualPos())
			servoLeg1.moveTimeWrite(direction*sin(t*2*pi/360)*angleStepLeg+initialPosL1);
			#servoLeg2.moveTimeWrite(direction*sin(t*2*pi/360)*angleStepLeg+initialPosL2);
			#servoArm1S.moveTimeWrite(direction*sin(4*t*2*pi/360)*angleStepShoulder+initialPosA1S);
			#servoArm1E.moveTimeWrite(direction*sin(4*t*2*pi/360)*angleStepElbow+initialPosA1E);
			servoArm2S.moveTimeWrite(-direction*sin(2*t*2*pi/360)*angleStepShoulder+initialPosA2S);
			servoArm2E.moveTimeWrite(-direction*sin(2*t*2*pi/360)*angleStepElbow+initialPosA2E);
			time.sleep(.01)	
			t+=5;
		direction= -direction;
	resetAllMotors(servoL1, servoL2, servoA1S, servoA1E, servoA2S, servoA2E)

def turnL1A1(servoLeg1, servoLeg2, servoArm1S, servoArm1E, servoArm2S, servoArm2E, 
	cycles, angleStepLeg, angleStepShoulder, angleStepElbow, r1, r2):
	print("Starting dance legs with arms")
	direction = 1;
	for i in range(0,cycles):
		t=0;

		initialPosL1 = servoLeg1.getPhysicalPos();
		initialPosL2 = servoLeg2.getPhysicalPos();

		initialPosA1S = servoArm1S.getPhysicalPos();
		initialPosA1E = servoArm1E.getPhysicalPos();

		initialPosA2S = servoArm2S.getPhysicalPos();
		initialPosA2E = servoArm2E.getPhysicalPos();

		while (t<180):
			r1.record();
			r2.record();
			# print(sin(t*2*pi/360)*angleStepLeg)
			# print("Motor id is ", servoLeg1.IDRead())
			# print("Physical pos is ", servoLeg1.getPhysicalPos())
			# print("Virtual pos is ", servoLeg1.getVirtualPos())
			# print("Motor id is ", servoLeg2.IDRead())
			# print("Physical pos is ", servoLeg2.getPhysicalPos())
			# print("Virtual pos is ", servoLeg2.getVirtualPos())
			servoLeg1.moveTimeWrite(direction*sin(t*2*pi/360)*angleStepLeg+initialPosL1);
			#servoLeg2.moveTimeWrite(direction*sin(t*2*pi/360)*angleStepLeg+initialPosL2);
			servoArm1S.moveTimeWrite(-direction*sin(2*t*2*pi/360)*angleStepShoulder+initialPosA1S);
			servoArm1E.moveTimeWrite(-direction*sin(2*t*2*pi/360)*angleStepElbow+initialPosA1E);
			# servoArm2S.moveTimeWrite(-direction*sin(4*t*2*pi/360)*angleStepShoulder+initialPosA2S);
			# servoArm2E.moveTimeWrite(-direction*sin(4*t*2*pi/360)*angleStepElbow+initialPosA2E);
			time.sleep(.01)	
			t+=5;
		direction= -direction;
	resetAllMotors(servoL1, servoL2, servoA1S, servoA1E, servoA2S, servoA2E)

def turnL2A1(servoLeg1, servoLeg2, servoArm1S, servoArm1E, servoArm2S, servoArm2E, 
	cycles, angleStepLeg, angleStepShoulder, angleStepElbow, r1, r2):
	print("Starting dance legs with arms")
	direction = 1;
	for i in range(0,cycles):
		t=0;

		initialPosL1 = servoLeg1.getPhysicalPos();
		initialPosL2 = servoLeg2.getPhysicalPos();

		initialPosA1S = servoArm1S.getPhysicalPos();
		initialPosA1E = servoArm1E.getPhysicalPos();

		initialPosA2S = servoArm2S.getPhysicalPos();
		initialPosA2E = servoArm2E.getPhysicalPos();

		while (t<180):
			r1.record();
			r2.record();
			# print(sin(t*2*pi/360)*angleStepLeg)
			# print("Motor id is ", servoLeg1.IDRead())
			# print("Physical pos is ", servoLeg1.getPhysicalPos())
			# print("Virtual pos is ", servoLeg1.getVirtualPos())
			# print("Motor id is ", servoLeg2.IDRead())
			# print("Physical pos is ", servoLeg2.getPhysicalPos())
			# print("Virtual pos is ", servoLeg2.getVirtualPos())
			#servoLeg1.moveTimeWrite(direction*sin(t*2*pi/360)*angleStepLeg+initialPosL1);
			servoLeg2.moveTimeWrite(direction*sin(t*2*pi/360)*angleStepLeg+initialPosL2);
			servoArm1S.moveTimeWrite(-direction*sin(2*t*2*pi/360)*angleStepShoulder+initialPosA1S);
			servoArm1E.moveTimeWrite(-direction*sin(2*t*2*pi/360)*angleStepElbow+initialPosA1E);
			#servoArm2S.moveTimeWrite(direction*sin(4*t*2*pi/360)*angleStepShoulder+initialPosA2S);
			#servoArm2E.moveTimeWrite(direction*sin(4*t*2*pi/360)*angleStepElbow+initialPosA2E);
			time.sleep(.01)	
			t+=5;
		direction= -direction;
	resetAllMotors(servoL1, servoL2, servoA1S, servoA1E, servoA2S, servoA2E)

def turnL2A2(servoLeg1, servoLeg2, servoArm1S, servoArm1E, servoArm2S, servoArm2E, 
	cycles, angleStepLeg, angleStepShoulder, angleStepElbow, r1, r2):
	print("Starting dance legs with arms")
	direction = 1;
	for i in range(0,cycles):
		t=0;

		initialPosL1 = servoLeg1.getPhysicalPos();
		initialPosL2 = servoLeg2.getPhysicalPos();

		initialPosA1S = servoArm1S.getPhysicalPos();
		initialPosA1E = servoArm1E.getPhysicalPos();

		initialPosA2S = servoArm2S.getPhysicalPos();
		initialPosA2E = servoArm2E.getPhysicalPos();

		while (t<180):
			r1.record();
			r2.record();
			# print(sin(t*2*pi/360)*angleStepLeg)
			# print("Motor id is ", servoLeg1.IDRead())
			# print("Physical pos is ", servoLeg1.getPhysicalPos())
			# print("Virtual pos is ", servoLeg1.getVirtualPos())
			# print("Motor id is ", servoLeg2.IDRead())
			# print("Physical pos is ", servoLeg2.getPhysicalPos())
			# print("Virtual pos is ", servoLeg2.getVirtualPos())
			#servoLeg1.moveTimeWrite(direction*sin(t*2*pi/360)*angleStepLeg+initialPosL1);
			servoLeg2.moveTimeWrite(direction*sin(t*2*pi/360)*angleStepLeg+initialPosL2);
			# servoArm1S.moveTimeWrite(-direction*sin(4*t*2*pi/360)*angleStepShoulder+initialPosA1S);
			# servoArm1E.moveTimeWrite(-direction*sin(4*t*2*pi/360)*angleStepElbow+initialPosA1E);
			servoArm2S.moveTimeWrite(direction*sin(2*t*2*pi/360)*angleStepShoulder+initialPosA2S);
			servoArm2E.moveTimeWrite(direction*sin(2*t*2*pi/360)*angleStepElbow+initialPosA2E);
			time.sleep(.01)	
			t+=5;
		direction= -direction;
	resetAllMotors(servoL1, servoL2, servoA1S, servoA1E, servoA2S, servoA2E)

def danceArmsAlternate(servoLeg1, servoLeg2, servoArm1S, servoArm1E, servoArm2S, servoArm2E, 
	cycles, angleStepLeg, angleStepShoulder, angleStepElbow, r1, r2):
	print("Starting dance legs with arms")
	direction = 1;
	for i in range(0,cycles):
		t=0;

		initialPosL1 = servoLeg1.getPhysicalPos();
		initialPosL2 = servoLeg2.getPhysicalPos();

		initialPosA1S = servoArm1S.getPhysicalPos();
		initialPosA1E = servoArm1E.getPhysicalPos();

		initialPosA2S = servoArm2S.getPhysicalPos();
		initialPosA2E = servoArm2E.getPhysicalPos();

		while (t<180):
			r1.record();
			r2.record();
			# print(sin(t*2*pi/360)*angleStepLeg)
			# print("Motor id is ", servoLeg1.IDRead())
			# print("Physical pos is ", servoLeg1.getPhysicalPos())
			# print("Virtual pos is ", servoLeg1.getVirtualPos())
			# print("Motor id is ", servoLeg2.IDRead())
			# print("Physical pos is ", servoLeg2.getPhysicalPos())
			# print("Virtual pos is ", servoLeg2.getVirtualPos())
			# servoLeg1.moveTimeWrite(direction*sin(t*2*pi/360)*angleStepLeg+initialPosL1);
			# servoLeg2.moveTimeWrite(direction*sin(t*2*pi/360)*angleStepLeg+initialPosL2);
			servoArm1S.moveTimeWrite(direction*sin(2*t*2*pi/360)*angleStepShoulder+initialPosA1S);
			servoArm1E.moveTimeWrite(direction*sin(2*t*2*pi/360)*angleStepElbow+initialPosA1E);
			time.sleep(.01)
			servoArm2S.moveTimeWrite(direction*sin(2*t*2*pi/360)*angleStepShoulder+initialPosA2S);
			servoArm2E.moveTimeWrite(direction*sin(2*t*2*pi/360)*angleStepElbow+initialPosA2E);
			time.sleep(.01)	
			t+=5;
		direction= -direction;
	resetAllMotors(servoL1, servoL2, servoA1S, servoA1E, servoA2S, servoA2E)

def danceArmsSynchronized(servoLeg1, servoLeg2, servoArm1S, servoArm1E, servoArm2S, servoArm2E, 
	cycles, angleStepLeg, angleStepShoulder, angleStepElbow, r1, r2):
	print("Starting dance legs with arms")
	direction = 1;
	for i in range(0,cycles):
		t=0;

		initialPosL1 = servoLeg1.getPhysicalPos();
		initialPosL2 = servoLeg2.getPhysicalPos();

		initialPosA1S = servoArm1S.getPhysicalPos();
		initialPosA1E = servoArm1E.getPhysicalPos();

		initialPosA2S = servoArm2S.getPhysicalPos();
		initialPosA2E = servoArm2E.getPhysicalPos();

		while (t<180):
			r1.record();
			r2.record();
			# print(sin(t*2*pi/360)*angleStepLeg)
			# print("Motor id is ", servoLeg1.IDRead())
			# print("Physical pos is ", servoLeg1.getPhysicalPos())
			# print("Virtual pos is ", servoLeg1.getVirtualPos())
			# print("Motor id is ", servoLeg2.IDRead())
			# print("Physical pos is ", servoLeg2.getPhysicalPos())
			# print("Virtual pos is ", servoLeg2.getVirtualPos())
			# servoLeg1.moveTimeWrite(direction*sin(t*2*pi/360)*angleStepLeg+initialPosL1);
			# servoLeg2.moveTimeWrite(direction*sin(t*2*pi/360)*angleStepLeg+initialPosL2);
			servoArm1S.moveTimeWrite(direction*sin(2*t*2*pi/360)*angleStepShoulder+initialPosA1S);
			servoArm1E.moveTimeWrite(direction*sin(2*t*2*pi/360)*angleStepElbow+initialPosA1E);
			time.sleep(.01)
			servoArm2S.moveTimeWrite(-direction*sin(2*t*2*pi/360)*angleStepShoulder+initialPosA2S);
			servoArm2E.moveTimeWrite(-direction*sin(2*t*2*pi/360)*angleStepElbow+initialPosA2E);
			time.sleep(.01)	
			t+=5;
		direction= -direction;
	resetAllMotors(servoL1, servoL2, servoA1S, servoA1E, servoA2S, servoA2E)

def danceLegsAndArms1(servoLeg1, servoLeg2, servoArm1S, servoArm1E, servoArm2S, servoArm2E, 
	cycles, angleStepLeg, angleStepShoulder, angleStepElbow, r1, r2):
	print("Starting dance legs with arms")
	direction = 1;
	for i in range(0,cycles):
		t=0;

		initialPosL1 = servoLeg1.getPhysicalPos();
		initialPosL2 = servoLeg2.getPhysicalPos();

		initialPosA1S = servoArm1S.getPhysicalPos();
		initialPosA1E = servoArm1E.getPhysicalPos();

		initialPosA2S = servoArm2S.getPhysicalPos();
		initialPosA2E = servoArm2E.getPhysicalPos();

		while (t<180):
			r1.record();
			r2.record();
			# print(sin(t*2*pi/360)*angleStepLeg)
			# print("Motor id is ", servoLeg1.IDRead())
			# print("Physical pos is ", servoLeg1.getPhysicalPos())
			# print("Virtual pos is ", servoLeg1.getVirtualPos())
			# print("Motor id is ", servoLeg2.IDRead())
			# print("Physical pos is ", servoLeg2.getPhysicalPos())
			# print("Virtual pos is ", servoLeg2.getVirtualPos())
			servoLeg1.moveTimeWrite(direction*sin(t*2*pi/360)*angleStepLeg+initialPosL1);
			servoLeg2.moveTimeWrite(direction*sin(t*2*pi/360)*angleStepLeg+initialPosL2);
			servoArm1S.moveTimeWrite(direction*sin(2*t*2*pi/360)*angleStepShoulder+initialPosA1S);
			servoArm1E.moveTimeWrite(direction*sin(2*t*2*pi/360)*angleStepElbow+initialPosA1E);
			servoArm2S.moveTimeWrite(direction*sin(2*t*2*pi/360)*angleStepShoulder+initialPosA2S);
			servoArm2E.moveTimeWrite(direction*sin(2*t*2*pi/360)*angleStepElbow+initialPosA2E);
			time.sleep(.01)	
			t+=5;
		direction= -direction;
	resetAllMotors(servoL1, servoL2, servoA1S, servoA1E, servoA2S, servoA2E)

def danceLegsAndArms2(servoLeg1, servoLeg2, servoArm1S, servoArm1E, servoArm2S, servoArm2E, 
	cycles, angleStepLeg, angleStepShoulder, angleStepElbow, r1, r2):
	print("Starting dance legs with arms")
	direction = 1;
	for i in range(0,cycles):
		t=0;

		initialPosL1 = servoLeg1.getPhysicalPos();
		initialPosL2 = servoLeg2.getPhysicalPos();

		initialPosA1S = servoArm1S.getPhysicalPos();
		initialPosA1E = servoArm1E.getPhysicalPos();

		initialPosA2S = servoArm2S.getPhysicalPos();
		initialPosA2E = servoArm2E.getPhysicalPos();

		while (t<180):
			r1.record();
			r2.record();
			# print(sin(t*2*pi/360)*angleStepLeg)
			# print("Motor id is ", servoLeg1.IDRead())
			# print("Physical pos is ", servoLeg1.getPhysicalPos())
			# print("Virtual pos is ", servoLeg1.getVirtualPos())
			# print("Motor id is ", servoLeg2.IDRead())
			# print("Physical pos is ", servoLeg2.getPhysicalPos())
			# print("Virtual pos is ", servoLeg2.getVirtualPos())
			servoLeg1.moveTimeWrite(direction*sin(t*2*pi/360)*angleStepLeg+initialPosL1);
			servoLeg2.moveTimeWrite(direction*sin(t*2*pi/360)*angleStepLeg+initialPosL2);
			servoArm1S.moveTimeWrite(direction*sin(2*t*2*pi/360)*angleStepShoulder+initialPosA1S);
			servoArm1E.moveTimeWrite(direction*sin(2*t*2*pi/360)*angleStepElbow+initialPosA1E);
			servoArm2S.moveTimeWrite(-direction*sin(2*t*2*pi/360)*angleStepShoulder+initialPosA2S);
			servoArm2E.moveTimeWrite(-direction*sin(2*t*2*pi/360)*angleStepElbow+initialPosA2E);
			time.sleep(.01)	
			t+=5;
		direction= -direction;
	resetAllMotors(servoL1, servoL2, servoA1S, servoA1E, servoA2S, servoA2E)

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

	servoL1.motorMode(800)
	servoL2.motorMode(-800)
	time.sleep(3)

	servoL1.servoMode()
	servoL2.servoMode()


	print("Resetting to home position")
	resetAllMotors(servoL1, servoL2, servoA1S, servoA1E, servoA2S, servoA2E)
	print("Finished resetting")
	

except KeyboardInterrupt:
	quit()
