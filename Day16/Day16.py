import re

detectableThings = ['children',
					'cats',
					'samoyeds',
					'pomeranians',
					'akitas',
					'vizslas',
					'goldfish',
					'trees',
					'cars',
					'perfumes']

detectedThings = {'children': 3,
				  'cats': 7,
				  'samoyeds': 2,
				  'pomeranians': 3,
				  'akitas': 0,
				  'vizslas': 0,
				  'goldfish': 5,
				  'trees': 3,
				  'cars': 2,
				  'perfumes': 1}

possibleMatches = []

with open('Day16Input.txt', 'r') as file:
	for line in file:
		line = line.strip()

		for thing in detectableThings:
			rawPattern = thing + r': (?P<num>[0-9]+)'
			pattern = re.compile(rawPattern)
			print(pattern)
			# print(re.match(pattern, line))


