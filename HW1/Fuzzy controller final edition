# ECE478 Homework 1
# Fuzzy Logic Simulation

from __future__ import division

class FuzzySet(object):
	def __init__(self, x1, x2):
		self.x1 = x1
		self.x2 = x2
	
	def membership(self, x, y):
		temp = int(y)
		if (temp == 100):
			if (x < self.x1 or x > self.x2):
				return 0.0
			elif (x > 0 and x <= 20):
				return 1
			elif (x > 20 and x <= 40):
				return 4/5
			elif (x > 40 and x <= 60):
				return 3/5
			elif (x > 60 and x <= 80):
				return 2/5
			elif (x > 80 and x <= 100):
				return 1/5
		
		if (temp == 180):
			if (x < self.x1 or x > self.x2):	
				return 0.0	
			if (x > 0 and x <= 60):	
				return 0.3	
			if (x > 60 and x <= 120):	
				return 1.0	
			if (x > 120 and x <= 180):	
				return 0.7	

def Main():
	# Settin up the input variables
	# Distance are measured in centimeters
	VeryClose	= FuzzySet(0, 20)
	Close	   	= FuzzySet(20, 40)
	Medium 		= FuzzySet(40, 60)
	Far 		= FuzzySet(60, 80)
	VeryFar		= FuzzySet(80,100)
	
	# Angles are measured in degrees
	Right   = FuzzySet(0, 60)
	Middle  = FuzzySet(60, 120)
	Left    = FuzzySet(120, 180)
	
	data = {}
	count = 0
	with open("fuzzy_data.txt","r") as fin:
		for line in fin:
			line = line.strip('\n')
			parts = line.split(',')
			temp = {}
			temp['Distance'] = int(parts[0])
			temp['Angle'] = int(parts[1])
			data[count] = temp
			count += 1

	for i in range(0,15):	
		Output_command = ""
		Output = 0.0

		Angle = float(data[i]['Angle'])
		Distance = float(data[i]['Distance'])
		# Fuzzification Rules
		Output += Middle.membership(Angle,180) * VeryFar.membership(Distance,100)
		Output += Middle.membership(Angle,180) * Far.membership(Distance,100)
		Output += Middle.membership(Angle,180) * Medium.membership(Distance,100)
		Output += Middle.membership(Angle,180) * Close.membership(Distance,100)
		Output += Middle.membership(Angle,180) * VeryClose.membership(Distance,100)
		
		Output += Right.membership(Angle,180) * VeryFar.membership(Distance,100)
		Output += Right.membership(Angle,180) * Far.membership(Distance,100)
		Output += Right.membership(Angle,180) * Medium.membership(Distance,100)
		Output += Right.membership(Angle,180) * Close.membership(Distance,100)
		Output += Right.membership(Angle,180) * VeryClose.membership(Distance,100)
		
		Output += Left.membership(Angle,180) * VeryFar.membership(Distance,100)
		Output += Left.membership(Angle,180) * Far.membership(Distance,100)
		Output += Left.membership(Angle,180) * Medium.membership(Distance,100)
		Output += Left.membership(Angle,180) * Close.membership(Distance,100)
		Output += Left.membership(Angle,180) * VeryClose.membership(Distance,100)

		# Defuzzification 
		if Output != 0:
			if Output == 0.42 or Output == 0.5599999999999999:
				Output_command = "Turn Right"
			elif Output == 0.24 or Output == 0.18:
				Output_command = "Turn Left"
			elif Output == 0.6 or Output == 0.8:
				Output_command = "Slow Down"
			elif Output == 0.3 or Output == 1.0 or Output == 0.7:
				Output_command = "Stop"
			else:
				Output_command = "MoveForward"

		print ("Distance: %f\tAngle: %f\nOutput_command %s" %(Distance, Angle, Output_command))
		print ("--------------------------------------------------------")
if __name__ == "__main__":
	Main()
