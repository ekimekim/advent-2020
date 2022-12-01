
import itertools
import sys

cups = {}

class Cup(object):
	__slots__ = ['label', 'next']
	def __init__(self, label):
		self.label = label
		cups[label] = self
		self.next = None

def append(cup, label):
	new_cup = Cup(label)
	cup.next = new_cup
	return new_cup

inputs = map(int, sys.stdin.read().strip())
current = Cup(inputs[0])
tail = current
max_label = 1000001

for input in inputs[1:]:
	tail = append(tail, input)
for i in range(max(inputs) + 1, 1000001):
	tail = append(tail, i)
tail.next = current

for _ in range(10000000):
	picked_up = current.next
	picked_up_labels = (
		picked_up.label,
		picked_up.next.label,
		picked_up.next.next.label,
	)
	current.next = picked_up.next.next.next
	for label in itertools.count(current.label - 1, -1):
		label = label % max_label
		if label != 0 and label not in picked_up_labels:
			dest_cup = cups[label]
			break
	picked_up.next.next.next = dest_cup.next
	dest_cup.next = picked_up
	current = current.next

print cups[1].next.label * cups[1].next.next.label
