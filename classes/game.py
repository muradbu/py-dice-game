class Game:
	def __init__(self, players, dice):
		self.players = players
		self.dice = dice

	def play(self):
		self.rollDice()
		self.announceScore()

	def rollDice(self):
		for player in self.players:
			player.rollDice(self.dice)

	def announceScore(self):
		for player in self.players:
			print(f"{player.name} rolled {player.diceOutcome}!")