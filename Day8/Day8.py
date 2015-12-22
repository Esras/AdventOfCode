import re as re

stringCodeCount = 0
memoryCount = 0

# Part 1
with open('Day8Input.txt', 'r') as file:
	for line in file:
		line = line.strip()

		memCountForLine = 0

		stringCodeCount += len(line)

		# Strip the " from either end
		line = line[1:-1]

		pattern = r'\\"'
		line = re.sub(pattern, 'A', line)

		pattern = r'\\\\'
		line = re.sub(pattern, 'B', line)

		pattern = r'\\[x][0-9a-f][0-9a-f]'
		line = re.sub(pattern, 'C', line)

		memCountForLine = len(line)

		memoryCount += memCountForLine

print("Difference: %s" % (stringCodeCount - memoryCount))

stringCodeCount = 0
newEncodedCount = 0

# Part 2
with open('Day8Input.txt', 'r') as file:
	for line in file:
		line = line.strip()

		stringCodeCount += len(line)

		line = line[1:-1]

		pattern = r'\\\"'
		line = re.sub(pattern, r'A', line)

		pattern = r'\\\\'
		line = re.sub(pattern, r'B', line)

		pattern = r'\"'
		line = re.sub(pattern, r'D', line)

		pattern = r'\\x'
		line = re.sub(pattern, r'C', line)


		line = line.replace('A', r'\\\"')
		line = line.replace('B', r'\\\\')
		line = line.replace('C', r'\\x')
		line = line.replace('D', r'\"')

		line = r'"\"' + line + r'"\"'
		print("%s: %s" % (line, len(line)))

		newEncodedCount += len(line)

print("Difference: %s" % (newEncodedCount - stringCodeCount))
