from operator import mul
from functools import reduce

totalSquareFootage = 0
totalRibbon = 0

with open('Day2Input.txt', 'r') as file:
	for line in file:
		line = line.strip()

		# Split on the x - we know that each line will be of the form #x#x#
		listOfNumsStr = line.split('x')

		# Turn each of those values into an integer and sort the list
		dimensions = [int(i) for i in listOfNumsStr]
		dimensions.sort()

		# print(dimensions)

		aSide = []

		# Only ever working in 3D space, so a cube
		aSide.append(dimensions[0] * dimensions[1])
		aSide.append(dimensions[0] * dimensions[2])
		aSide.append(dimensions[1] * dimensions[2])
		aSide.sort() # Sort for upcoming ribbon

		for side in aSide:
			totalSquareFootage += 2 * side

		totalSquareFootage += aSide[0] # Only need to add the smallest face for the slack in wrapping paper

		totalRibbon += 2 * (dimensions[0] + dimensions[1])
		totalRibbon += reduce(mul, dimensions)

print("Total Wrapping Paper with Extra: %s" % totalSquareFootage)
print("Total Ribbon with Extra: %s" % totalRibbon)