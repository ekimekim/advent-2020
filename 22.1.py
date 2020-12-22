
import sys

p1, p2 = [
	map(int, p.split("\n")[1:])
	for p in sys.stdin.read().strip().split("\n\n")
]

def step(p1, p2):
	c1, c2 = p1.pop(0), p2.pop(0)
	winner = p1 if c1 > c2 else p2
	winner.extend(sorted([c1, c2], reverse=True))

def score(deck):
	return sum(
		(i+1) * c
		for i, c in enumerate(deck[::-1])
	)

while p1 and p2:
	step(p1, p2)

print score(p1 if p1 else p2)
