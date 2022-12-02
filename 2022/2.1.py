
import sys

strats = [
	line.split()
	for line in sys.stdin.read().strip().split("\n")
]

def score(theirs, ours):
	theirs = ord(theirs) - ord('A')
	ours = ord(ours) - ord('X')
	result = (1 + ours - theirs) % 3
	return 1 + ours + 3 * result

print sum(score(a, b) for a, b in strats)
