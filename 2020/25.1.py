import sys
from itertools import count

def transform(subject, loop):
	value = 1
	for _ in range(loop):
		value = (value * subject) % 20201227
	return value

def find_loop(subject, target):
	value = 1
	for i in count(1):
		value = (value * subject) % 20201227
		if value == target:
			return i

card_key, door_key = map(int, sys.stdin.read().strip().split('\n'))

card_loop = find_loop(7, card_key)
enc_key = transform(door_key, card_loop)

print enc_key
