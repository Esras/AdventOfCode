from collections import defaultdict
import re

replacements = defaultdict(list)
molecule = ''
finalMolecules = []

with open('Day19Input.txt', 'r') as file:
	for line in file:
		line = line.strip()

		if '=>' not in line:
			#print('Final Molecule: \'%s\'' % line)
			molecule = line
		else:
			molecules = line.split(' => ')
			replacements[molecules[0]].append(molecules[1])
			#print('Replace %s with %s' % (molecules[0], molecules[1]))

for key in replacements:
	#print("Finding: %s" % key)
	for replacement in replacements[key]:
		for match in re.finditer(key, molecule):
			#print(molecule.replace(match, replacements[key]))
			#print(match)
			newMolecule = molecule[0:match.start()]
			newMolecule += replacement
			newMolecule += molecule[match.end():]
			#print("New molecule: %s" % newMolecule)
			# Look https://docs.python.org/3/library/re.html#match-objects for stuff on the match object returned
			finalMolecules.append(newMolecule)

print("Distinct molecules: %s" % len(set(finalMolecules)))

# Info for part 2:
# https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju

# Find all of the molecules - they all start with a capital letter
pattern = r'[A-Z]'
numAtoms = len(re.findall(pattern, molecule))
print("Num Atoms: %s" % numAtoms)

pattern = r'(?:Rn)|(?:Ar)'
numParens = len(re.findall(pattern, molecule))
print("Num of Rn or Ar: %s" % numParens)

pattern = r'Y'
numCommas = len(re.findall(pattern, molecule))
print("Num Y: %s" % numCommas)

# Final count
finalCount = numAtoms - numParens - 2 * numCommas - 1
print("Final steps: %s" % finalCount)