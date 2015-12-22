from collections import defaultdict
from pprint import pprint
from itertools import permutations
import re

guestHappinessDict = defaultdict(dict)
guestList = []
possibleSeatings = []
potentialHappiness = []

# Build the dictionary of distances
with open('Day13Input.txt', 'r') as file:
	for line in file:
		line = line.strip()

		firstGuest = line.split(' would ')[0]
		secondGuest = line.split(' to ')[1][:-1]

		pattern = r'[0-9]+'
		happiness = int(re.findall(pattern, line)[0])
		print("happiness of %s sitting next to %s is: %s" % (firstGuest, secondGuest, happiness))

		if 'lose' in line:
			happiness *= -1

		guestHappinessDict[firstGuest][secondGuest] = happiness

		if firstGuest not in guestList:
			guestList.append(firstGuest)

pprint(guestHappinessDict)

# Create all possible combinations of people around the table
for permutation in permutations(guestList, len(guestList)):
	possibleSeatings.append(permutation)

pprint(possibleSeatings)

for seating in possibleSeatings:
	iterationTotal = 0
	for i in range(len(seating)):
		primeGuest = seating[i]
		if i == 0:
			leftGuest = seating[len(seating) - 1]
		else:
			leftGuest = seating[i - 1]
		iterationTotal += guestHappinessDict[primeGuest][leftGuest]

		if i == len(seating) - 1:
			rightGuest = seating[0]
		else:
			rightGuest = seating[i + 1]
		iterationTotal += guestHappinessDict[primeGuest][rightGuest]

	potentialHappiness.append(iterationTotal)


print(max(potentialHappiness))
