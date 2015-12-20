
totalSquareFootage = 0

with open('Day2Input.txt', 'r') as file:
	for line in file:
		line = line.strip()

		listOfNumsStr = line.split('x')

		dimensions = [int(i) for i in listOfNumsStr]

#		print(dimensions)

		aSide = []

		# Only ever working in 3D space, so a cube
		aSide.append(dimensions[0] * dimensions[1])
		aSide.append(dimensions[0] * dimensions[2])
		aSide.append(dimensions[1] * dimensions[2])

		for side in aSide:
			totalSquareFootage += 2 * side

		totalSquareFootage += min(aSide)

print(totalSquareFootage)