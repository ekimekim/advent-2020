import sys

lines = sys.stdin.read().strip().split("\n")

t = 0
for line in lines:
	card, numbers = line.split(": ")
	wins, mine = numbers.split(" | ")
	wins = set(map(int, wins.split()))
	mine = set(map(int, mine.split()))
	got = len(mine & wins)
	if got:
		t += 2**(got - 1)
print t
