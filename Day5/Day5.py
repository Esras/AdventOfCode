niceCountPart1 = 0
niceCountPart2 = 0

with open('Day5Input.txt', 'r') as file:
	for line in file:
		line = line.strip()

		# Part 1
		consecutiveRequirement = False
		badStringFound = False

		# Check bad strings
		badStrings = ["ab", "cd", "pq", "xy"]
		for bs in badStrings:
			if line.count(bs):
				badStringFound = True

		for i in range(len(line) - 1):
			if line[i] == line[i + 1]:
				consecutiveRequirement = True

		# Time to count vowels...
		vowelList = ['a', 'e', 'i', 'o', 'u']
		vowelCount = 0
		for character in line:
			if character in vowelList:
				vowelCount += 1

		if not badStringFound:
			if consecutiveRequirement:
				if vowelCount >= 3:
					niceCountPart1 += 1

		properPairedLetters = False;
		properSpacingRepeated = False;

		# Part 2
		for i in range(len(line) - 1):
			tempString = line[i] + line[i + 1]
			if line.count(tempString) > 1:
				properPairedLetters = True
				# print("Found proper pairing in %s with %s" % (line, tempString))
				break

		for i in range(len(line) - 2):
			if line[i] == line[i + 2]:
				properSpacingRepeated = True;
				# print("Found proper spacing in %s with %s" % (line, line[i:i+3]))
				break

		if properPairedLetters:
			if properSpacingRepeated:
				niceCountPart2 += 1;


print("Nice Strings in part 1: %s" % niceCountPart1)
print("Nice Strings in part 1: %s" % niceCountPart2)