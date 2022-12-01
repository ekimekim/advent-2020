import sys
from collections import Counter
import itertools

seats = [
	list(line.strip())
	for line in sys.stdin
]

def cast(seats, x, y, dx, dy):
	while True:
		x += dx
		y += dy
		if x < 0 or y < 0 or y >= len(seats) or x >= len(seats[y]):
			return False
		c = seats[y][x]
		if c != '.':
			return c == '#'

DELTAS = [
	(dx, dy)
	for dx, dy in itertools.product((-1, 0, 1), (-1, 0, 1))
	if dx != 0 or dy != 0
]

def step(seats, prev_dirty_box):
	new_seats = [list(line) for line in seats]
	dirty_box = [[len(seats[0]) - 1, len(seats) - 1], [0, 0]]
	for y in range(prev_dirty_box[0][1], prev_dirty_box[1][1] + 1):
		for x in range(prev_dirty_box[0][0], prev_dirty_box[1][0] + 1):
			if seats[y][x] == '.':
				continue
			elif seats[y][x] == 'L':
				for dx, dy in DELTAS: 
					if cast(seats, x, y, dx, dy):
						break
				else:
					new_seats[y][x] = '#'
					dirty_box[0][0] = max(0, min(dirty_box[0][0], x - 1))
					dirty_box[0][1] = max(0, min(dirty_box[0][1], y - 1))
					dirty_box[1][0] = min(len(seats[0]) - 1, max(dirty_box[1][0], x + 1))
					dirty_box[1][1] = min(len(seats) - 1, max(dirty_box[1][1], y + 1))
			else:
				count = 0
				for dx, dy in DELTAS:
					if cast(seats, x, y, dx, dy):
						count += 1
						if count == 5:
							new_seats[y][x] = 'L'
							dirty_box[0][0] = max(0, min(dirty_box[0][0], x - 1))
							dirty_box[0][1] = max(0, min(dirty_box[0][1], y - 1))
							dirty_box[1][0] = min(len(seats[0]) - 1, max(dirty_box[1][0], x + 1))
							dirty_box[1][1] = min(len(seats) - 1, max(dirty_box[1][1], y + 1))
							break

	return new_seats, dirty_box

def p(seats):
	print '\n'.join(''.join(line) for line in seats)

dirty_box = [[0, 0], [len(seats[0]) - 1, len(seats) - 1]]
while True:
	print dirty_box
	new_seats, dirty_box = step(seats, dirty_box)
#	p(new_seats)
#	print
	if seats == new_seats:
		break
	seats = new_seats
	

print Counter(seats[y][x] for y in range(len(seats)) for x in range(len(seats[0])))['#']
