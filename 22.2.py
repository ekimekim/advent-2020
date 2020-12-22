
import os
import sys

p1, p2 = [
	tuple(map(int, p.split("\n")[1:]))
	for p in sys.stdin.read().strip().split("\n\n")
]

def play(p1, p2):
	seen = set()
	subgame = 0
	while p1 and p2:
		# identical prev round -> p1 win
		if (p1, p2) in seen:
			return 1, p1
		seen.add((p1, p2))
		c1, p1 = p1[0], p1[1:]
		c2, p2 = p2[0], p2[1:]
		if len(p1) >= c1 and len(p2) >= c2:
			# both cards left >= card drawn, recurse
			winner, winning_deck = play(p1[:c1], p2[:c2])
		else:
			# play normally
			winner = 1 if c1 > c2 else 2
		if winner == 1:
			p1 += (c1, c2)
		else:
			p2 += (c2, c1)
	return (1, p1) if p1 else (2, p2)

def score(deck):
	return sum(
		(i+1) * c
		for i, c in enumerate(deck[::-1])
	)

winner, winning_deck = play(p1, p2)
print score(winning_deck)
