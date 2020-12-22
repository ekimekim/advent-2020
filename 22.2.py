
import os
import sys

p1, p2 = [
	tuple(map(int, p.split("\n")[1:]))
	for p in sys.stdin.read().strip().split("\n\n")
]

def debug(game, *args):
	if 'DEBUG' in os.environ:
		print ".".join(map(str,game)), ":", " ".join(map(str, args))

def play(p1, p2, game=()):
	seen = set()
	subgame = 0
	while p1 and p2:
		debug(game, "start round:", p1, p2)
		# identical prev round -> p1 win
		if (p1, p2) in seen:
			debug(game, (p1, p2), "seen before, p1 wins")
			return 1, p1
		seen.add((p1, p2))
		c1, p1 = p1[0], p1[1:]
		c2, p2 = p2[0], p2[1:]
		debug(game, p1, "->", c1, "|", p2, "->", c2)
		if len(p1) >= c1 and len(p2) >= c2:
			# both cards left >= card drawn, recurse
			debug(game, "beginning subgame with decks:", p1[:c1], p2[:c2])
			winner, winning_deck = play(p1[:c1], p2[:c2], game=game+(subgame,))
			debug(game, "subgame result:", winner, winning_deck)
			subgame += 1
		else:
			# play normally
			winner = 1 if c1 > c2 else 2
			debug(game, "normal result:", winner)
		if winner == 1:
			p1 += (c1, c2)
		else:
			p2 += (c2, c1)
	debug(game, "player out of cards,", (1 if p1 else 2), "wins with", (p1 if p1 else p2))
	return (1, p1) if p1 else (2, p2)

def score(deck):
	return sum(
		(i+1) * c
		for i, c in enumerate(deck[::-1])
	)

winner, winning_deck = play(p1, p2)
print score(winning_deck)
