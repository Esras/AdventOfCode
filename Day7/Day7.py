from pprint import pprint

wireDict = {}
wireDone = {}

complete = False

listOfCommands = []
inputAndOutputList = []

BITWISE_TRUNCATION_BITS = 0xFFFF

PART_1_ANSWER = 46065
PART_2 = True

def Store(key, value):
	if value is not False:
		wireDict[key] = value
		wireDone[key] = True
		return True
	return False


def IntOrFalse(s):
    try:
        return int(s)
    except ValueError:
        return False
    except TypeError:
    	return False


def TryToGetIntFromDictTwoSides(lhs, rhs):

	leftInt = IntOrFalse(lhs)
	rightInt = IntOrFalse(rhs)

	if leftInt is False:
		leftInt = IntOrFalse(wireDict[lhs])

	if rightInt is False:
		rightInt = IntOrFalse(wireDict[rhs])

	return leftInt, rightInt


def CanPerformTwoInputOp(lhs, rhs):

	if lhs is not False:
		if rhs is not False:
			return True

	return False


# Grab all of the lines and put them into a list
with open('Day7Input.txt', 'r') as file:
	for line in file:
		line = line.strip()

		listOfCommands.append(line)

# Split the list into inputs and outputs
for item in listOfCommands:
	splitLine = item.split('->')
	input = splitLine[0].strip()
	output = splitLine[1].strip()
	inputAndOutputList.append([input, output])

# Let's go ahead and put all of the outputs into a dict so we can track what has value and what doesn't
for item in inputAndOutputList:
	wireDict[item[1]] = item[0].split(' ')
	wireDone[item[1]] = False

# If we're running part 2, override line b
if PART_2:
	wireDict['b'] = PART_1_ANSWER
	wireDone['b'] = True

while not complete:
	# Keep running - let's avoid recursion

	numDone = 0

	for key in wireDict:
		if wireDone[key]:
			numDone += 1
			for deeperKey in wireDict:
				if not wireDone[deeperKey]:
					for i in range(len(wireDict[deeperKey])):
						if key == wireDict[deeperKey][i]:
							wireDict[deeperKey][i] = wireDict[key]
							pprint(wireDict)
			continue

		storageValue = 0

		# Input will only ever be of three possibilities
		#   1. Value
		#   2. NOT Value
		#   3. Value1 AND Value2

		# Handle the direct storage case
		if len(wireDict[key]) == 1:
			storageValue = IntOrFalse(wireDict[key][0])
			if Store(key, storageValue):
				continue

		# Handle the NOT case
		if len(wireDict[key]) == 2:
			# Look up the dict, if we can NOT it
			storageValue = IntOrFalse(wireDict[key][1])
			if storageValue is not False:
				storageValue = ~storageValue
			if Store(key, storageValue):
				continue
			else:
				# We're here because the value in the dict wasn't an int
				# So the next possibility is that it was ['NOT', 'aa'] in which case we want to check the
				# dictionary again to see if aa has an int stored in it
				newKey = wireDict[key][1]
				storageValue = IntOrFalse(wireDict[newKey])
				if storageValue is not False:
					storageValue = ~storageValue
				if Store(key, storageValue):
					continue

		# Handle the other cases
		if len(wireDict[key]) == 3:
			lhs = wireDict[key][0]
			rhs = wireDict[key][2]
			operation = wireDict[key][1]

			# Go through the arduous task of trying to get ints from the dict
			lhs, rhs = TryToGetIntFromDictTwoSides(lhs, rhs)

			# If they aren't ints, one or both of these is now False.
			if not CanPerformTwoInputOp(lhs, rhs):
				continue

			if 'LSHIFT' in operation:
				storageValue = (lhs << rhs) & BITWISE_TRUNCATION_BITS

			elif 'RSHIFT' in operation:
				storageValue = (lhs >> rhs) & BITWISE_TRUNCATION_BITS

			elif 'AND' in operation:
				storageValue = lhs & rhs

			elif 'OR' in operation:
				storageValue = lhs | rhs

			else:
				print("Unknown operation!")

			if Store(key, storageValue):
				continue

	complete = True
	for key in wireDict:
		if not wireDone[key]:
			complete = False
			break

pprint(wireDict)
