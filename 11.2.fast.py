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

neighbors = [None for _ in range(len(seats))]
def cast(seats, x, y, dx, dy):
	while True:
		x += dx
		y += dy
		if x < 0 or y < 0 or y >= COL_LEN or x >= ROW_LEN:
			return None
		c = seats[y * ROW_LEN + x]
		if c != '.':
			return x, y
for y in range(COL_LEN):
	for x in range(ROW_LEN):
		found = []
		for dx, dy in itertools.product((-1, 0, 1), (-1, 0, 1)):
			if dx == 0 and dy == 0:
				continue
			neighbor = cast(seats, x, y, dx, dy)
			if neighbor:
				found.append(neighbor)
		neighbors[y * ROW_LEN + x] = found


def step(seats):
	new_seats = seats[:]
	for y in range(COL_LEN):
		for x in range(ROW_LEN):
			if seats[y * ROW_LEN + x] == '.':
				continue
			elif seats[y * ROW_LEN + x] == 'L':
				for nx, ny in neighbors[y * ROW_LEN + x]: 
					if seats[ny * ROW_LEN + nx] == '#':
						break
				else:
					new_seats[y * ROW_LEN + x] = '#'
			else:
				count = 0
				for nx, ny in neighbors[y * ROW_LEN + x]: 
					if seats[ny * ROW_LEN + nx] == '#':
						count += 1
						if count == 5:
							new_seats[y * ROW_LEN + x] = 'L'
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
	

print Counter(seats)['#']
