import itertools
import re
from pprint import pprint
from collections import defaultdict

NUM_TEASPOONS = 100
ingredientDict = defaultdict(dict)
ingredients = []
scores = []

PART_2 = True

with open('Day15Input.txt', 'r') as file:
	for line in file:
		line = line.strip()

		ingredientName = line.split(':')[0]
		ingredients.append(ingredientName)

		pattern = r'-?[0-9]'
		rawNumbers = re.findall(pattern, line)

		ingredientDict[ingredientName]['capacity']   = int(rawNumbers[0])
		ingredientDict[ingredientName]['durability'] = int(rawNumbers[1])
		ingredientDict[ingredientName]['flavor']     = int(rawNumbers[2])
		ingredientDict[ingredientName]['texture']    = int(rawNumbers[3])
		ingredientDict[ingredientName]['calories']   = int(rawNumbers[4])

for combo in itertools.combinations_with_replacement(ingredients, NUM_TEASPOONS):

	propertyScore = defaultdict(dict)
	for ingredient in set(combo):
		numOfIngredient = combo.count(ingredient)

		for property in ingredientDict[ingredient]:
			propertyScore[property][ingredient] = numOfIngredient * ingredientDict[ingredient][property]

	cookieScore = 1
	calorieCount = 0
	for property in propertyScore:

		runningSum = 0
		for score in propertyScore[property]:
			runningSum += propertyScore[property][score]

		if runningSum < 0:
			runningSum = 0

		if property != 'calories':
			cookieScore *= runningSum
		else:
			calorieCount = runningSum

	if PART_2:
		if calorieCount == 500:
			scores.append(cookieScore)
	else:
		scores.append(cookieScore)


print("Max score: %s" % max(scores))