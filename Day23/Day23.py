import re

class Program:

	instructions = []

	currentInstruction = 0
	programLength = 0

	registers = {'a': 0,
				 'b': 0}

	def __init__(self, file):
		with open(file, 'r') as file:
			for line in file:
				line = line.strip()
				self.instructions.append(re.split(r'[ ,]+', line))
		self.programLength = len(self.instructions)
		print(self.instructions)

	def ExecuteProgram(self):
		while self.currentInstruction < self.programLength:
			print("Executing at: %s" % self.currentInstruction)
			self.ExecuteInstruction(self.instructions[self.currentInstruction])

	def ExecuteInstruction(self, instruction):

		op = instruction[0]
		print("op: %s" % op)
		curRegisterValue = 0
		incrementBy = 1 # Set to the default

		# Start with jump ops
		if op == 'jmp':
			incrementBy = self.Jump(int(instruction[1]))
		else:
			register = instruction[1]
			curRegisterValue = int(self.registers[register])

		if op == 'jie':
			incrementBy = self.JumpIfEven(curRegisterValue, int(instruction[2]))
		elif op == 'jio':
			incrementBy = self.JumpIfOne(curRegisterValue, int(instruction[2]))
		elif op == 'inc':
			curRegisterValue = self.IncrementRegister(curRegisterValue)
			self.registers[register] = curRegisterValue
		elif op == 'hlf':
			curRegisterValue = self.HalfRegister(curRegisterValue)
			self.registers[register] = curRegisterValue
		elif op == 'tpl':
			curRegisterValue = self.TripleRegister(curRegisterValue)
			self.registers[register] = curRegisterValue

		self.IncrementInstructionBy(incrementBy)

	def IncrementInstructionBy(self, incrementBy):
		self.currentInstruction += incrementBy

	def HalfRegister(self, register):
		return register / 2

	def TripleRegister(self, register):
		return register * 3

	def IncrementRegister(self, register):
		return register + 1

	def Jump(self, offset):
		return offset

	def JumpIfEven(self, register, offset):
		incrementBy = 0
		if register % 2 == 0:
			incrementBy = offset
		else:
			incrementBy = 1
		return incrementBy

	def JumpIfOne(self, register, offset):
		incrementBy = 0
		if register == 1:
			incrementBy = offset
		else:
			incrementBy = 1
		return incrementBy

input = Program('Day23Input.txt')

input.ExecuteProgram()

print(input.registers)