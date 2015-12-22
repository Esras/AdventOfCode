import re

def IncrementString(str):

	lastChar = str[-1]
	rolloverCount = 0

	while lastChar == 'z':
		rolloverCount += 1
		if not rolloverCount == len(str):
			lastChar = str[-1 - rolloverCount]
		else:
			return 'a' * (rolloverCount + 1)

	nextChar = chr(ord(lastChar) + 1)

	if rolloverCount > 0:
		newString = str[:-1 - rolloverCount] + nextChar + ('a' * rolloverCount)
	else:
		newString = str[:-1] + nextChar

	return newString


def CheckCharRequirement(str):

	if re.search(r'[iol]', str) is None:
		return True

	return False


def CheckForConsecutive(str):
	incrementPattern = False
	location = 0
	consecutiveCount = 1

	while not incrementPattern:
		if location + 1 > len(str) - 1: # Location tracks index, length is tracking size
			return False
		char = str[location]
		nextChar = str[location + 1]
		expChar = chr(ord(char) + 1)
		#print("char: %s nextChar: %s expChar: %s" % (char, nextChar, expChar))
		if nextChar == expChar:
			#print("Incremented consecutiveCount on %s %s" % (nextChar, expChar))
			consecutiveCount += 1
		else:
			consecutiveCount = 1
		location += 1
		if consecutiveCount == 3:
			return True

	return False


def CheckForRepeatingChars(str):
	matches = re.findall(r'([a-z])\1', str)
	if len(set(matches)) >= 2:
		return True
	else:
		return False


def CheckValidity(str):

	if not CheckCharRequirement(str):
		return False
	elif not CheckForConsecutive(str):
		return False
	elif not CheckForRepeatingChars(str):
		return False
	else:
		return True


with open('Day11Input.txt', 'r') as file:
	for line in file:
		password = line.strip()

		print("Original Password: %s" % password)

		passwordValid = False

		while not passwordValid:
			password = IncrementString(password)
			passwordValid = CheckValidity(password)

		print("Next Password: %s" % password)