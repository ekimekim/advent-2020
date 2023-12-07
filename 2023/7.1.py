import sys
from collections import Counter

def strength(hand):
	value = lambda c: -"AKQJT98765432".index(c) # negative sign means smaller index is higher
	counts = sorted(Counter(hand).values(), reverse=True)
	# the rules are such that hand type order is the same thing as lexiographic order
	# of the counts list. ie. [5] > [4,1] > [3,2] > [3,1,1] > [2,2,1] > [2,1,1,1] > [1,1,1,1,1]
	return counts, map(value, hand)

cards = [line.split() for line in sys.stdin.read().strip().split("\n")]
cards.sort(key=lambda (hand, bid): strength(hand))

print sum((i+1) * int(bid) for i, (hand, bid) in enumerate(cards))
