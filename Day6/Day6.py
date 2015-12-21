dimension = 1000
numLightsLit = 0

lightGrid = [0] * dimension
for i in range(dimension):
	lightGrid[i] = [0] * dimension

TURN_OFF = 0
TURN_ON  = 1
TOGGLE   = 2

option = TURN_OFF

def manipulateLights(manipOption, beginTuple, endTuple):

	beginList = [int(i) for i in beginTuple.split(',')]
	endList = [int(i) for i in endTuple.split(',')]

	lightsChanged = 0

	for i in range(endList[0] - beginList[0] + 1):
		for j in range(endList[1] - beginList[1] + 1):
			if manipOption is TURN_OFF:
				lightGrid[beginList[0] + i][beginList[1] + j] = 0;
			elif manipOption is TURN_ON:
				lightGrid[beginList[0] + i][beginList[1] + j] = 1;
			elif manipOption is TOGGLE:
				lightGrid[beginList[0] + i][beginList[1] + j] = not lightGrid[beginList[0] + i][beginList[1] + j]
			else:
				print("OH NOES!")
			lightsChanged += 1

	# print("Lights changed: %s" % lightsChanged)


with open('Day6Input.txt', 'r') as file:
	for line in file:
		line = line.strip()

		splitList = line.split(' ')
		#print(splitList)

		if splitList[0] == 'turn':
			if splitList[1] == 'on':
				# print("Turning on")
				option = TURN_ON
			elif splitList[1] == 'off':
				# print("Turning off")
				option = TURN_OFF
			manipulateLights(option, splitList[2], splitList[4])
		elif splitList[0] == 'toggle':
			# print("Toggling")
			manipulateLights(TOGGLE, splitList[1], splitList[3])
		else:
			print("ERMAGHERD!")

	for i in range(dimension):
		for j in range(dimension):
			if lightGrid[i][j]:
				numLightsLit += 1

	print("Number of lights lit: %s" % numLightsLit)