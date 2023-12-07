import sys
from collections import Counter

def strength(hand):
	value = lambda c: -"AKQT98765432J".index(c) # negative sign means smaller index is higher
	by_count = Counter(hand)
	# Joker adjustment: the best kind to be is always the same as the most popular other kind,
	# or in other words add its count to the largest count otherwise.
	jokers = by_count.pop("J", 0)
	counts = sorted(by_count.values(), reverse=True)
	if jokers == 5:
		# special case: no non jokers!
		counts = [5]
	else:
		counts[0] += jokers
	# the rules are such that hand type order is the same thing as lexiographic order
	# of the counts list. ie. [5] > [4,1] > [3,2] > [3,1,1] > [2,2,1] > [2,1,1,1] > [1,1,1,1,1]
	return counts, map(value, hand)

cards = [line.split() for line in sys.stdin.read().strip().split("\n")]
cards.sort(key=lambda (hand, bid): strength(hand))

print sum((i+1) * int(bid) for i, (hand, bid) in enumerate(cards))
