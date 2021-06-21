from classes.game import Game
from classes.die import Die
from classes.player import Player
import argparse

def main():
	args = parseArgs()
	game = Game(addPlayers(args["name"]), addDice(args["dice"], args["faces"]))
	game.play()

def parseArgs():
	parser = argparse.ArgumentParser()

	parser.add_argument("-n", "--name", type=str)
	parser.add_argument("-d", "--dice", nargs="?", default=2, type=int)
	parser.add_argument("-f", "--faces", nargs="?", default=6, type=int)

	args = vars(parser.parse_args())

	if "name" in args.keys():
		args["name"] = [s.strip() for s in args["name"].split(",")]

	return args

def addPlayers(names):
	players = []
	for name in names:
		players.append(Player(name))

	return players

def addDice(diceAmount, faceAmount):
	dice = []
	for _ in range(diceAmount):
		dice.append(Die(faceAmount))

	return dice

main()