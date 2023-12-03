import sys

MAX = {
	"red": 12,
	"green": 13,
	"blue": 14,
}

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
	possible = True
	for color, limit in MAX.items():
		if any(game.get(color, 0) > limit for game in games):
			possible = False
	if possible:
		total += id

print total
