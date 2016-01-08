# ----------------------------------------------------------------------------------------------------------------------
# Character
#   Description:
#     Base class for defining a character of some sort in this mini-game.  It could be used to extend this even futher.
#     There might be some sort of NPC or minion that had other characteristics.  But for now, we just have bosses and
#     players.
#
# ----------------------------------------------------------------------------------------------------------------------
class Character:

	def __init__(self, HP, MP, DEF):
		"""Create a character with some basic stats and a list of effects"""
		self.currentEffects = []
		self.HP = HP
		self.Mana = MP
		self.Armor = DEF

# ----------------------------------------------------------------------------------------------------------------------
# Wizard (Extends Character)
#
#   Description:
#     Defines a wizard in this game.  Wizards have a list of spells they can cast.
#
# ----------------------------------------------------------------------------------------------------------------------
class Wizard(Character):

	def __init__(self, HP, MP, DEF, spells):
		super().__init__(HP, MP, DEF)
		self.spellList = spells

# ----------------------------------------------------------------------------------------------------------------------
# Boss (Extends Character)
#   Description:
#     Defines a boss in this game.  Bosses add a basic damage swing.
#
# ----------------------------------------------------------------------------------------------------------------------
class Boss(Character):

	def __init__(self, HP, MP, DEF, DMG):
		super().__init__(HP, MP, DEF)
		self.damage = DMG

# ----------------------------------------------------------------------------------------------------------------------
# Spell
#   Description:
#     Defines a spell.  Spells are defined by their effects, their name, their mana cost, how many turns the effect will
#     last, and the magnitude of the effect.  Effects have to be known by the system, as indicated by the effectList in
#     the class.  The other thing to note is that this current model doesn't allow for different magnitudes for
#     different effects.
#
# ----------------------------------------------------------------------------------------------------------------------
class Spell:

	effectList = ["None", "Damage HP", "Restore HP", "Restore MP", "Increase DEF"]

	def __init__(self, name, cost, turns, effects, magnitude):
		self.effectType = []
		for effect in effects:
			if effect not in Spell.effectList:
				raise Exception("Effect %s not in list!" % effect)
			else:
				self.effectType.append(effect)
		self.name = name
		self.manaCost = cost
		self.numTurns = turns
		self.effectMagnitude = magnitude


# ----------------------------------------------------------------------------------------------------------------------
# Spell
#   Description:
#     A spell instance stores a reference back to a spell, so that it can calculate its effect on the character that the
#     spell instance is attached to.
#
# ----------------------------------------------------------------------------------------------------------------------
class SpellInstance:

	def __init__(self, spell):
		self.spell = spell
		self.numTurnsRemaining = spell.numTurns

	def Tick(self):
		numTurns -= 1


# Define all of the spells
magicMissiles = Spell("Magic Missiles", 53,  0, ["Damage HP"],               4)
drain         = Spell("Drain",          73,  0, ["Damage HP", "Restore HP"], 2)
shield        = Spell("Shield",         113, 6, ["Increase DEF"],            7)
poison        = Spell("Poison",         173, 6, ["Damage HP"],               3)
recharge      = Spell("Recharge",       229, 5, ["Restore MP"],              101)

playerSpells = []
playerSpells.append(magicMissiles)
playerSpells.append(drain)
playerSpells.append(shield)
playerSpells.append(poison)
playerSpells.append(recharge)

# Player and Boss information and definitions
playerHP = 10
playerMana = 250
playerArmor = 0
# playerHP = 10
# playerMP = 250

bossHP = 1
3bossDMG = 8
# bossHP = 71
# bossDMG = 10

player = Wizard(playerHP, playerMana, playerArmor, playerSpells)
boss = Boss(bossHP, bossMana, bossArmor, bossDMG)

# Actual calculations