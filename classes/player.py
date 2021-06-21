class Player:
	money = 200
	diceOutcome = []

	def __init__(self, name):
		self.name = name

	def rollDice(self, dice):
		for die in dice:
			outcome = die.roll()
			self.diceOutcome.append(outcome)