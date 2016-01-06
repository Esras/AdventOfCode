from itertools import permutations, combinations, takewhile

packages = []
weight = 0
NUM_COMPARTMENTS = 4
minPackages = 100000 # Arbitrarily large
quantumEntanglementOfMin = 0

def CalculateQE(packageList):
	QE = 1
	for pkg in packageList:
		QE *= pkg
	return QE

with open('Day24Input.txt', 'r') as file:
	for line in file:
		line = line.strip()
		packages.append(int(line))
	weight = sum(packages) / NUM_COMPARTMENTS
	print("Target weight: %s" % weight)

# for iter in permutations(packages):
# 	iter = list(iter)
# 	# Start by seeing if you can sum the first
# 	firstGroupSlice = 0
# 	firstGroupWeight = 0
# 	while firstGroupWeight < weight:
# 		firstGroupSlice += 1
# 		firstGroupWeight = sum(iter[0:firstGroupSlice])

# 	if firstGroupWeight > weight:
# 		continue

# 	secondGroupSlice = firstGroupSlice
# 	secondGroupWeight = 0
# 	while secondGroupWeight < weight:
# 		secondGroupSlice += 1
# 		secondGroupWeight = sum(iter[firstGroupSlice:secondGroupSlice])

# 	if secondGroupWeight > weight:
# 		continue

# 	firstGroup  = iter[0:firstGroupSlice]
# 	# secondGroup = iter[firstGroupSlice:secondGroupSlice]
# 	# thirdGroup  = iter[secondGroupSlice:]

# 	if len(firstGroup) < minPackages:
# 		minPackages = len(firstGroup)
# 		quantumEntanglement = CalculateQE(firstGroup)
# 		print("%s Packages with %s entanglement" % (minPackages, quantumEntanglementOfMin))
# 	elif quantumEntanglement < quantumEntanglementOfMin:
# 		quantumEntanglementOfMin = quantumEntanglement
# 		print("  New entanglement: %s" % quantumEntanglementOfMin)

# 	# numPackages = len(firstGroup)
# 	# quantumEntanglement = CalculateQE(firstGroup)

# 	# print("First group: %s with weight %s" % (firstGroup, sum(firstGroup)))
# 	# print("Second group: %s with weight %s" % (secondGroup, sum(secondGroup)))
# 	# print("Third group: %s with weight %s" % (thirdGroup, sum(thirdGroup)))

qe = 10000000000000000
storei = 10000

for i in range(1, len(packages)):
	if i > storei:
		break

	for firstGroup in combinations(packages, i):
		firstGroup = list(firstGroup)
		if sum(firstGroup) != weight:
			continue

		reducedList = []
		for x in packages:
			if x not in firstGroup:
				reducedList.append(x)

		for j in range(1, len(reducedList)):
			for secondGroup in combinations(reducedList, j):
				secondGroup = list(secondGroup)
				if sum(secondGroup) != weight:
					continue

				curQE = CalculateQE(firstGroup)
				if curQE < qe:
					qe = curQE
					print(qe)
					storei = i
