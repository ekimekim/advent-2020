import sys
from collections import Counter
import itertools

seats = [
	list(line.strip())
	for line in sys.stdin
]
ROW_LEN = len(seats[0])
COL_LEN = len(seats)
seats = sum(seats, [])

def cast(seats, x, y, dx, dy):
	while True:
		x += dx
		y += dy
		if x < 0 or y < 0 or y >= COL_LEN or x >= ROW_LEN:
			return False
		c = seats[y * ROW_LEN + x]
		if c != '.':
			return c == '#'

DELTAS = [
	(dx, dy)
	for dx, dy in itertools.product((-1, 0, 1), (-1, 0, 1))
	if dx != 0 or dy != 0
]

def step(seats):
	new_seats = seats[:]
	for y in range(COL_LEN):
		for x in range(ROW_LEN):
			if seats[y * ROW_LEN + x] == '.':
				continue
			elif seats[y * ROW_LEN + x] == 'L':
				for dx, dy in DELTAS: 
					if cast(seats, x, y, dx, dy):
						break
				else:
					new_seats[y * ROW_LEN + x] = '#'
			else:
				count = 0
				for dx, dy in DELTAS:
					if cast(seats, x, y, dx, dy):
						count += 1
						if count == 5:
							new_seats[y * ROW_LEN + x] = 'L'
							break

	return new_seats


while True:
	new_seats = step(seats)
	if seats == new_seats:
		break
	seats = new_seats
	

print Counter(seats)['#']
