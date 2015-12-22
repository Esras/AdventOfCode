import re

totalTime = 2503
distances = []

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

		# We know how long it takes to complete a full cycle for a reindeer
		cycleTime = reindeerRestTime + reindeerSpeedTime
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
