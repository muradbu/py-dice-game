import random as r

class Die:
	def __init__(self, faces):
		self.faces = faces

	def roll(self):
		return r.randint(1, self.faces)