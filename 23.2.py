import sys
import itertools

cups = map(int, sys.stdin.read().strip())
max_cup = max(cups)
max_label = 1000001
cups += range(max_cup + 1, max_label)

def step(index):
	picked_up = cups[index+1:index+4]
#	print "picked up", picked_up, "from", index+1, "to", index+4
	for label in itertools.count(cups[index] - 1, -1):
		label = label % max_label
		if label != 0 and label not in picked_up:
			dest_cup = label
			break
	dest_index = cups.index(dest_cup)
#	print "count down from", cups[index], "to", dest_cup, "at", dest_index

	to_move = (dest_index - index - 3) % len(cups)
#	print "moving", to_move, "down"
	for i in range(index + 1, index + 1 + to_move):
#		print "cups[{}] = {} -> {}".format(i % len(cups), cups[i % len(cups)], cups[(i + 3) % len(cups)])
		cups[i % len(cups)] = cups[(i + 3) % len(cups)]
	for i in range(3):
#		print "cups[{}] = {} -> {}".format((index + 1 + to_move + i) % len(cups), cups[(index + 1 + to_move + i) % len(cups)], picked_up[i])
		cups[(index + 1 + to_move + i) % len(cups)] = picked_up[i]

for i in range(10000000):
	print "{:.2f}%".format(i / 100000.)
	step(i % len(cups))

one_index = cups.index(1)
print cups[(one_index + 1) % len(cups)] * cups[(one_index + 2) % len(cups)]
