import re as re

stringCodeCount = 0
memoryCount = 0

with open('Day8Input.txt', 'r') as file:
	for line in file:
		line = line.strip()

		memCountForLine = 0

		stringCodeCount += len(line)

		# Strip the " from either end
		line = line[1:-1]

		pattern = r'\\"'
		line = re.sub(pattern, 'S', line)

		pattern = r'\\\\'
		line = re.sub(pattern, 'A', line)

		pattern = r'\\[x][0-9a-fA-F][0-9A-Fa-f]'
		line = re.sub(pattern, 'C', line)

		memCountForLine = len(line)

		memoryCount += memCountForLine

print("Difference: %s" % (stringCodeCount - memoryCount))