
import sys

strats = [
	line.split()
	for line in sys.stdin.read().strip().split("\n")
]

def score(theirs, result):
	theirs = ord(theirs) - ord('A')
	result = ord(result) - ord('X')
	ours = (theirs + result - 1) % 3
	return 1 + ours + 3 * result

print sum(score(a, b) for a, b in strats)
