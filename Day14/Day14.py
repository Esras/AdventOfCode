import re
from collections import defaultdict

totalTime = 2503
distances = []
points = {}
reindeerSpeedDict = defaultdict(dict)

# Part 1
with open('Day14Input.txt', 'r') as file:
	for line in file:
		line = line.strip()

		reindeerName = line.split(' can ')[0]
		print("%s" % reindeerName)

		pattern = r'[0-9]+'
		rawNumbers = re.findall(pattern, line)
		reindeerSpeed     = int(rawNumbers[0])
		reindeerSpeedTime = int(rawNumbers[1])
		reindeerRestTime  = int(rawNumbers[2])

		reindeerSpeedDict[reindeerName]['speed']     = reindeerSpeed
		reindeerSpeedDict[reindeerName]['speedTime'] = reindeerSpeedTime
		reindeerSpeedDict[reindeerName]['restTime']  = reindeerRestTime
		reindeerSpeedDict[reindeerName]['distance']  = 0
		reindeerSpeedDict[reindeerName]['points']    = 0

		# We know how long it takes to complete a full cycle for a reindeer
		cycleTime = reindeerRestTime + reindeerSpeedTime
		reindeerSpeedDict[reindeerName]['cycleTime'] = cycleTime
		print("  Cycle time is %s s" % cycleTime)

		# Figure out how many complete cycles happen for this reindeer
		numberOfCycles = totalTime // (reindeerSpeedTime + reindeerRestTime)
		print("  %s full cycles" % numberOfCycles)

		# If they completed a cycle, then we add that to their distance
		reindeerDistance = numberOfCycles * reindeerSpeedTime * reindeerSpeed

		timeRemaining = totalTime - (numberOfCycles * cycleTime)
		print("  %s s remain" % timeRemaining)
		timeRemaining = min(timeRemaining, reindeerSpeedTime)
		print("  %s s more of travel time" % timeRemaining)

		reindeerDistance += reindeerSpeed * timeRemaining
		print("  %s km total distance" % reindeerDistance)

		distances.append(reindeerDistance)

print("Furthest distance traveled in Part 1: %s km" % max(distances))

for i in range(totalTime):

	for reindeerName in reindeerSpeedDict:
		curCycleTime = i % reindeerSpeedDict[reindeerName]['cycleTime']

		# Check if the reindeer is resting
		if curCycleTime < reindeerSpeedDict[reindeerName]['speedTime']:
			# We're only doing a second as our timestep, so add a speed to our distance
			reindeerSpeedDict[reindeerName]['distance'] += reindeerSpeedDict[reindeerName]['speed']

	leadDistance = 0
	for reindeerName in reindeerSpeedDict:
		curDistance = reindeerSpeedDict[reindeerName]['distance']
		if curDistance > leadDistance:
			leadDistance = curDistance

	print("Lead distance: %s" % leadDistance)

	for reindeerName in reindeerSpeedDict:
		if reindeerSpeedDict[reindeerName]['distance'] == leadDistance:
			print("Gave point to %s" % reindeerName)
			reindeerSpeedDict[reindeerName]['points'] += 1

for reindeerName in reindeerSpeedDict:
	print("%s: %s points" % (reindeerName, reindeerSpeedDict[reindeerName]['points']))