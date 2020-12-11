import sys
from collections import Counter
import itertools

seats = [
	list(line.strip())
	for line in sys.stdin
]

def get(seats, x, y):
	if x < 0 or y < 0 or y >= len(seats) or x >= len(seats[y]):
		return ''
	return seats[y][x]

def step(seats):
	new_seats = [list(line) for line in seats]
	for y in range(len(new_seats)):
		for x in range(len(new_seats[y])):
			if seats[y][x] == '.':
				continue
			c = Counter(
				get(seats, x+dx, y+dy)
				for dx, dy in itertools.product((-1, 0, 1), (-1, 0, 1))
				if dx != 0 or dy != 0
			)
			if seats[y][x] == 'L' and c['#'] == 0:
				new_seats[y][x] = '#'
			elif seats[y][x] == '#' and c['#'] >= 4:
				new_seats[y][x] = 'L'
	return new_seats

def p(seats):
	print '\n'.join(''.join(line) for line in seats)

while True:
	new_seats = step(seats)
	p(new_seats)
	if seats == new_seats:
		break
	seats = new_seats
	

print Counter(seats[y][x] for y in range(len(seats)) for x in range(len(seats[0])))['#']
