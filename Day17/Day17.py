import itertools

containers = []
eggnogQuantity = 150
potentialCombos = 0
minContainerCount = 100
numberOfMinContainerCombos = 0
comboList = []

with open('Day17Input.txt', 'r') as file:
	for line in file:
		line = line.strip()

		containers.append(int(line))

for i in range(len(containers)):
	for combo in itertools.combinations(containers, i):
		if sum(combo) == eggnogQuantity:
			if len(combo) < minContainerCount:
				minContainerCount = len(combo)
			potentialCombos += 1
			comboList.append(combo)

for combo in comboList:
	if len(combo) == minContainerCount:
		numberOfMinContainerCombos += 1

print("Potential combos in part 1: %s" % potentialCombos)
print("Number of combos of min count: %s" % numberOfMinContainerCombos)
