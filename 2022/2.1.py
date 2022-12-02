
import sys

strats = [
	line.split()
	for line in sys.stdin.read().strip().split("\n")
]

def score(a, b):
	result = (1 + (ord(b) - ord("X")) - (ord(a) - ord("A"))) % 3
	return 1 + "XYZ".index(b) + 3 * result

print sum(score(a, b) for a, b in strats)
