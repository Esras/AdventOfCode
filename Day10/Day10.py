NUM_PERMUTATIONS = 50

with open('Day10Input.txt', 'r') as file:
	for line in file:
		number = line.strip()

		for _ in range(NUM_PERMUTATIONS):
			nextNumber = ''
			i = 0
			while i < len(number):
				curDigit = number[i]
				count = 1
				while i + count < len(number) and curDigit == number[i + count]:
					count += 1

				nextNumber += str(count)
				nextNumber += curDigit
				i += count

			number = nextNumber

print(len(number))
