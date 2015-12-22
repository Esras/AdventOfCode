from collections import defaultdict
from pprint import pprint
from itertools import permutations

distanceDict = defaultdict(dict)
cityList = []
possibleRoutes = []
routeDistances = []

# Build the dictionary of distances
with open('Day9Input.txt', 'r') as file:
	for line in file:
		line = line.strip()

		rawSplitLine = line.split(' to ')
		startCity = rawSplitLine[0]
		destAndDist = rawSplitLine[1].split(' = ')
		endCity = destAndDist[0]
		distance = int(destAndDist[1])

		distanceDict[startCity][endCity] = distance
		distanceDict[endCity][startCity] = distance

		if startCity not in cityList:
			cityList.append(startCity)
		elif endCity not in cityList:
			cityList.append(endCity)

# Create all possible routes
for permutation in permutations(cityList, len(cityList)):
	possibleRoutes.append(permutation)

# Compute the length of the routes
for route in possibleRoutes:
	routeDistance = 0
	for i in range(len(route) - 1):
		routeDistance += distanceDict[route[i]][route[i + 1]]

	routeDistances.append(routeDistance)

print(min(routeDistances))
