import json

PART_2 = True
ignoreKey = 'red'

def process(thing):
	tempVar = 0
	if isinstance(thing, dict):
		for key in thing:
			if PART_2 and key == ignoreKey:
				tempVar = 0
				break
			elif PART_2 and thing[key] == ignoreKey:
				tempVar = 0
				break
			tempVar += process(thing[key])
	elif isinstance(thing, list):
		for i in range(len(thing)):
			tempVar += process(thing[i])
	elif isinstance(thing, int):
		tempVar = thing

	return tempVar


pyJSON = json.load(open('Day12Input.json','r'))

sum = process(pyJSON)
print("Sum: %s" % sum)