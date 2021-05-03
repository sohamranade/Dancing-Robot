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

		self.initialTemp = int(self.servo.tempRead())
		self.initialVoltage = int(self.servo.vInRead())
		self.maxTemp = initialTemp+30
		self.maxVoltage = initialVoltage+1000
		self.minVoltage = initialVoltage-1000;
	def record(self):
		self.id.append(int(self.servo.IDRead()))
		self.angleOffset.append(int(self.servo.angleOffsetRead()))
		self.physicalPos.append(int(self.servo.getPhysicalPos()))
		self.virtualPos.append(int(self.servo.getVirtualPos()))
		self.temp.append(int(self.servo.tempRead()))
		self.voltage.append(int(self.servo.vInRead()))
	def resetMotor(self):
		servo1 = self.servo;
		targetPos = 120;
		initialPos = servo1.getPhysicalPos();
		error = targetPos-initialPos

		print(servo1.IDRead())
		print(initialPos)
		print(error)

		t=0;
		while (abs(sin(t*2*pi/360)*error) < abs(error)):
			print("Motor id is ", servo1.IDRead())
			print("Physical pos is ", servo1.getPhysicalPos())
			print("Virtual pos is ", servo1.getVirtualPos())
			servo1.moveTimeWrite(sin(t*2*pi/360)*error+initialPos)
			time.sleep(.01)
			t+=2

		if abs(servo1.getPhysicalPos() - 120) > 20:
			raise Exception("Initial position is not 120")

		self.checkHealth();
	def checkHealth(self):
		currTemp = int(self.servo.tempRead());
		currVoltage = int(self.servo.vInRead());
		if (currTemp > self.maxTemp):
			raise Exception("Temperature is too high, ", currTemp);
		if (currVoltage > self.maxVoltage):
			raise Exception("Voltage is too high, ", currVoltage);
		if (currVoltage < self.minVoltage):
			raise Exception("Voltage is too low, ", currVoltage);

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

def danceLegs1(servo1, servo2,cycles, relativeAngleStep, r1, r2):
	print("Starting dance 1")
	direction = 1;
	for i in range(0,cycles):
		t=0;
		initialPos1 = servo1.getPhysicalPos();
		initialPos2 = servo2.getPhysicalPos();
		while (abs(sin(t*2*pi/360)*relativeAngleStep) < relativeAngleStep):
			r1.record();
			r2.record();
			print(sin(t*2*pi/360)*relativeAngleStep)
			print("Motor id is ", servo1.IDRead())
			print("Physical pos is ", servo1.getPhysicalPos())
			print("Virtual pos is ", servo1.getVirtualPos())
			print("Motor id is ", servo2.IDRead())
			print("Physical pos is ", servo2.getPhysicalPos())
			print("Virtual pos is ", servo2.getVirtualPos())
			servo1.moveTimeWrite(direction*sin(t*2*pi/360)*relativeAngleStep+initialPos1);
			servo2.moveTimeWrite(direction*sin(t*2*pi/360)*relativeAngleStep+initialPos2);
			time.sleep(.01)	
			t+=5;
		direction= -direction;

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

	r1 = RecordMotorData(servo1);
	r2 = RecordMotorData(servo2);

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

	r1.record()
	r2.record()

	print("Starting initialization")
	r1.resetMotor();
	r2.resetMotor();
	print("End initialization")

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
	
	r1.record()
	r2.record()

	danceLegs1(servo1, servo2, 4, 40, r1, r2)
	r1.checkHealth();
	r2.checkHealth();

	print("Resetting to home position")
	r1.resetMotor();
	r2.resetMotor();
	print("Finished resetting")

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
	
	r1.record()
	r2.record()

	print("Finished recording")

	print("Starting to save")
	motorDataList = [];
	motorDataList.append(r1);
	motorDataList.append(r2);
	save2CSV(motorDataList)
	print("Finished saving")
	

except KeyboardInterrupt:
	quit()
