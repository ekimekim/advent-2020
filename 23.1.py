import sys
import itertools

cups = map(int, sys.stdin.read().strip())
max_label = max(cups) + 1

def step(cups):
	picked_up, cups = cups[1:4], cups[:1] + cups[4:]
	for label in itertools.count(cups[0] - 1, -1):
		label = label % max_label
		if label in cups:
			dest_cup = label
			break
	dest_index = cups.index(dest_cup)
	cups = cups[:dest_index+1] + picked_up + cups[dest_index+1:]
	cups = cups[1:] + cups[:1]
	return cups

for _ in range(100):
	cups = step(cups)
	print cups

one_index = cups.index(1)
print "".join(map(str, cups[one_index+1:] + cups[:one_index]))
