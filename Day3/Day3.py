with open('Day3Input.txt', 'r') as file:
	for line in file:
		line = line.strip()

		santaPos = [(0, 0)]

		curXPos = 0
		curYPos = 0

		for character in line:
			if character is '<':
				curXPos += 1
			elif character is '>':
				curXPos -= 1
			elif character is '^':
				curYPos += 1
			elif character is 'v':
				curYPos	-= 1
			santaPos.append((curXPos, curYPos))

		# Grid I used for figuring out the next calculation
		# There will always be a dimension of 1 - Santa starts on the first square
		# But, the bounds don't just scale based on how many he goes right or left.  After all, Santa could just cycle
		# between two houses.  It's the difference between the two that dictates how it scales
		#
		# >>^^vvvv gives:
		#
		#     x x 5
		#     x x 6
		#     1 2 7
		#     x x 8
		#     x x 9

		uniqueHouses = list(set(santaPos))
		print("Unique houses visited: %s" % len(uniqueHouses))



		# Everything below here is garbage, but I'm leaving it for posterity's sake

		# houseGrid = [0] * horizDimen
		# for i in range(horizDimen):
		# 	houseGrid[i] = [0] * vertDimen

		# # Now for his position.  He will start at 0, 0 (in the case of not moving)
		# # For every movement that extends the bounds to the right and up, it does not affect his starting location
		# # Example:
		# #
		# # 	  >>^^ produces:
		# #
		# #         x x 4
		# #         x x 3
		# #         S 1 2
		# #
		# #     Santa still starts at 0, 0.
		# #
		# #     But if he instead does <<vv:
		# #
		# #         2 1 S
		# #         3 x x
		# #         4 x x
		# #
		# #     Santa now starts at 2, 2 (indexing at 0).
		# #
		# # This means that the only thing affecting his starting location are the negative moves that extend the board,
		# # meaning that we only care about the maximum negative value.
		# #
		# # Example:
		# #
		# #     ><<vv^:
		# #
		# #         3 S 1
		# #         6 x x
		# #         5 x x
		# #
		# #     Santa starts at 1, 2 (most negative in x was -1 and most negative in y was -2)

		# curXPos = abs(min(xPosSanta))
		# curYPos = abs(min(yPosSanta))

		# # Don't forget the first house got a present:
		# houseGrid[curXPos][curYPos] += 1

		# for character in line:
		# 	if character is '<':
		# 		curXPos += 1
		# 	elif character is '>':
		# 		curXPos -= 1
		# 	elif character is '^':
		# 		curYPos += 1
		# 	elif character is 'v':
		# 		curYPos -= 1

		# 	houseGrid[curXPos][curYPos] += 1

		# numHousesWithPresents = 0

		# for x in range(horizDimen):
		# 	for y in range(vertDimen):
		# 		if houseGrid[x][y] > 0:
		# 			numHousesWithPresents += 1

		# print("Number of houses with presents: %s" % numHousesWithPresents)

