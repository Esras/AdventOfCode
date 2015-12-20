with open('Day1Input.txt', 'r') as file:
	for line in file:
		line = line.strip()

		count = 0
		charNum = 0;

		openParenCount = line.count('(')
		closeParenCount = line.count(')')
		print("Floor: " + str(openParenCount - closeParenCount))

		for character in line:
			charNum += 1
			if character == '(':
				count += 1
			elif character == ')':
				count -= 1
			else:
				print("Something went wrong!")

			if count < 0:
				print("Entered the basement at " + str(charNum))
				break

