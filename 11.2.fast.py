import sys
import os
from collections import Counter
import itertools

TIMED = os.environ.get('TIMED')
if TIMED:
	from monotonic import monotonic

seats = [
	list(line.strip())
	for line in sys.stdin
]
ROW_LEN = len(seats[0])
COL_LEN = len(seats)
seats = sum(seats, [])

if TIMED:
	precast = monotonic()

DELTAS = [
	(dx, dy)
	for dx, dy in itertools.product((-1, 0, 1), (-1, 0, 1))
	if dx != 0 or dy != 0
]
DELTAS = [
	(-1, 0), # left
	(-1, -1), # up-left
	(0, -1), # up
	(1, -1), # up-right
]

neighbors = [None for _ in range(len(seats))]
for index, char in enumerate(seats):
	if char == '.':
		continue
	y, x = divmod(index, ROW_LEN)
	# note we only ever raycast upwards,
	# we get the other direction by reversing the relation when we find someone
	found = []
	for dx, dy in DELTAS:
		nx = x + dx
		ny = y + dy
		while nx >= 0 and ny >= 0 and nx < ROW_LEN:
			c = seats[ny * ROW_LEN + nx]
			if c != '.':
				break
			nx += dx
			ny += dy
		else:
			continue

		# add both pairs. note the other neighbor is always behind us, so it's already
		# got a list
		found.append((nx, ny))
		neighbors[ny * ROW_LEN + nx].append((x, y))
	neighbors[index] = found

if TIMED:
	postcast = monotonic()
	print "Cast cache took:", postcast - precast

def step(seats):
	new_seats = seats[:]
	for index, char in enumerate(seats):
		if char == '.':
			continue
		elif char == 'L':
			for nx, ny in neighbors[index]: 
				if seats[ny * ROW_LEN + nx] == '#':
					break
			else:
				new_seats[index] = '#'
		else:
			count = 0
			for nx, ny in neighbors[index]: 
				if seats[ny * ROW_LEN + nx] == '#':
					count += 1
					if count == 5:
						new_seats[index] = 'L'
						break

	return new_seats

def p(seats):
	for y in range(COL_LEN):
		print ''.join(seats[y * COL_LEN : (y+1) * COL_LEN])

while True:
	new_seats = step(seats)
	# p(new_seats)
	if seats == new_seats:
		break
	seats = new_seats

if TIMED:
	postrun = monotonic()
	print "Run took:", postrun - postcast

print Counter(seats)['#']

if TIMED:
	print "Count took:", monotonic() - postrun
