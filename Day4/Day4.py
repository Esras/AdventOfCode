import hashlib

secretKey = 'ckczppom'
stringForHash = ''
encodedString = stringForHash.encode('utf-8')

digest = 'abcdef123456789' # Random number
# Answer for me for part 1 was 117946
i = 0

numChars = 6

while digest[:numChars] != '0'*numChars:
	i += 1
	stringForHash = secretKey + str(i)

	# print(stringForHash)
	encodedString = stringForHash.encode('utf-8')

	digest = hashlib.md5(encodedString).hexdigest()

	if i % 1000000 is 0:
		print(i)


print(i)