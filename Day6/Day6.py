dimension = 1000
numLightsLit = 0

lightGrid = [0] * dimension
for i in range(dimension):
	lightGrid[i] = [0] * dimension

TURN_OFF = 0
TURN_ON  = 1
TOGGLE   = 2

PART_1 = 0
PART_2 = 1

option = TURN_OFF
mode = PART_2

def manipulateLights(manipOption, beginTuple, endTuple, mode):

	beginList = [int(i) for i in beginTuple.split(',')]
	endList = [int(i) for i in endTuple.split(',')]

	lightsChanged = 0

	xOffset = beginList[0]
	yOffset = beginList[1]

	for i in range(endList[0] - xOffset + 1):
		for j in range(endList[1] - yOffset + 1):
			if manipOption is TURN_OFF:
				if mode == PART_1:
					nextValue = 0
				elif mode == PART_2:
					nextValue = -1
			elif manipOption is TURN_ON:
				if mode == PART_1:
					nextValue = 1
				elif mode == PART_2:
					nextValue = 1
			elif manipOption is TOGGLE:
				if mode == PART_1:
					nextValue = not lightGrid[xOffset + i][yOffset + j]
				elif mode == PART_2:
					nextValue = 2
			else:
				print("OH NOES!")


			if mode == PART_1:
				lightGrid[xOffset + i][yOffset + j] = nextValue
			elif mode == PART_2:
				lightGrid[xOffset + i][yOffset + j] += nextValue

				if lightGrid[xOffset + i][yOffset + j] < 0:
					lightGrid[xOffset + i][yOffset + j] = 0

			else:
				print("MORE MADNESS!")

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
			manipulateLights(option, splitList[2], splitList[4], mode)
		elif splitList[0] == 'toggle':
			# print("Toggling")
			manipulateLights(TOGGLE, splitList[1], splitList[3], mode)
		else:
			print("ERMAGHERD!")

	for i in range(dimension):
		for j in range(dimension):
			if mode == PART_1:
				if lightGrid[i][j]:
					numLightsLit += 1
			elif mode == PART_2:
				numLightsLit += lightGrid[i][j]

	if mode == PART_1:
		print("Number of lights lit: %s" % numLightsLit)
	elif mode == PART_2:
		print("Brightness of lights lit: %s" % numLightsLit)
