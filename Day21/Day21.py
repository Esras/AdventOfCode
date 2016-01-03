import itertools
from math import ceil

shopInventory = {
	'Dagger':{
		'Cost':8,
		'Damage':4,
		'Armor':0
	},
	'Shortsword':{
		'Cost':10,
		'Damage':5,
		'Armor':0
	},
	'Warhammer':{
		'Cost':25,
		'Damage':6,
		'Armor':0
	},
	'Longsword':{
		'Cost':40,
		'Damage':7,
		'Armor':0
	},
	'Greataxe':{
		'Cost':74,
		'Damage':8,
		'Armor':0
	},
	'Nothing':{
		'Cost': 0,
		'Damage': 0,
		'Armor': 0
	},
	'Leather':{
		'Cost': 13,
		'Damage':0,
		'Armor':1
	},
	'Chainmail':{
		'Cost': 31,
		'Damage':0,
		'Armor':2
	},
	'Splintmail':{
		'Cost': 53,
		'Damage':0,
		'Armor':3
	},
	'Bandedmail':{
		'Cost': 75,
		'Damage':0,
		'Armor':4
	},
	'Platemail':{
		'Cost': 102,
		'Damage':0,
		'Armor':5
	},
	'Damage +1':{
		'Cost':25,
		'Damage':1,
		'Armor':0
	},
	'Damage +2':{
		'Cost':50,
		'Damage':2,
		'Armor':0
	},
	'Damage +3':{
		'Cost':100,
		'Damage':3,
		'Armor':0
	},
	'Defense +1':{
		'Cost':20,
		'Damage':0,
		'Armor':1
	},
	'Defense +2':{
		'Cost':40,
		'Damage':0,
		'Armor':2
	},
	'Defense +3':{
		'Cost':80,
		'Damage':0,
		'Armor':3
	}
}

def swing(attack, defense):
	damage = attack - defense
	if damage < 1:
		damage = 1
	return damage

listOfWeapons = ["Dagger", "Shortsword", "Warhammer", "Longsword", "Greataxe"]
listOfArmor   = ["Nothing", "Leather", "Chainmail", "Splintmail", "Bandedmail", "Platemail"]
listOfRings   = ["Damage +1", "Damage +2", "Damage +3", "Defense +1", "Defense +2", "Defense +3"]

# Player Info (Player goes first)
playerHP    = 100
playerDMG   = 0
playerArmor = 0

maxRings        = 2
playerInventory = []
lowestCost      = 1000000 # Arbitrarily large value
highestCost     = 0


# Boss Info
bossHP    = 103
bossDMG   = 9
bossArmor = 2

for weapon in listOfWeapons:
	for armor in listOfArmor:
		for numRings in range(0, maxRings + 1):
			for ringSelection in itertools.combinations(listOfRings, numRings):
				# Build the player's inventory
				playerInventory.append(weapon)
				playerInventory.append(armor)
				for ring in list(ringSelection):
					playerInventory.append(ring)

				# Build the player's stats
				playerCost  = 0
				playerDMG   = 0
				playerArmor = 0
				for item in playerInventory:
					playerCost  += shopInventory[item]['Cost']
					playerDMG   += shopInventory[item]['Damage']
					playerArmor += shopInventory[item]['Armor']

				# Battle calculation
				damage = playerDMG - bossArmor
				if damage <= 0:
					damage = 1
				numTurnsForPlayerToWin = ceil(bossHP / damage)

				damage = bossDMG - playerArmor
				if damage <= 0:
					damage = 1
				numTurnsForBossToWin = ceil(playerHP / damage)

				# Check who won and store gold
				if numTurnsForPlayerToWin <= numTurnsForBossToWin:
					if playerCost < lowestCost:
						lowestCost = playerCost
				else:
					if playerCost > highestCost:
						highestCost = playerCost


				playerInventory = []

print("Lowest cost and win: %i" % lowestCost)
print("Highest cost and lose: %i" % highestCost)