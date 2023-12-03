import sys

COLORS = "red", "green", "blue"

total = 0
for line in sys.stdin.read().strip().split("\n"):
	header, games = line.split(": ")
	_, id = header.split()
	id = int(id)
	games = [
		{
			part.split()[1]: int(part.split()[0])
			for part in game.split(", ")
		} for game in games.split("; ")
	]
	required = {
		color: max(game.get(color, 0) for game in games)
		for color in COLORS
	}
	power = 1
	for color in COLORS:
		power *= required[color]
	total += power

print total
