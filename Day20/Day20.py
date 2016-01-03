from math import sqrt

puzzleNumber = 33100000
sum = 0

# Because I was looking for a quick version of this, I pulled the factor code from:
# http://rosettacode.org/wiki/Factors_of_an_integer#Python
def factor(n):
	factors = set()
	for x in range(1, int(sqrt(n)) + 1):
		if n % x == 0:
			factors.add(x)
			factors.add(n//x)
	return factors

print("Original number: %s" % puzzleNumber)

for i in range(0, int(puzzleNumber / 2)):
	sum = 0
	factorList = factor(i)
	print(i)
	for j in factorList:
		sum += j
	sum *= 10
	print("  Sum: %i" % sum)
	print("  Ori: %i" % puzzleNumber)
	if sum >= puzzleNumber:
		print(factorList)
		break
