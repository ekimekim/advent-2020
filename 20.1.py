
import itertools
import sys
from collections import namedtuple

Tile = namedtuple('Tile', ['id', 'border_options'])
FixedTile = namedtuple('FixedTile', ['id', 'borders'])
Borders = namedtuple('Borders', ['top', 'right', 'bottom', 'left'])

def parse_tile(tile):
	id = int(tile.split('\n')[0].split()[1][:-1])
	rows = tile.split('\n')[1:]
	borders = Borders(
		rows[0],
		"".join(row[-1] for row in rows),
		rows[-1],
		"".join(row[0] for row in rows),
	)
	# this is a horizontal flip
	flipped = Borders(
		borders[0][::-1],
		borders[3],
		borders[2][::-1],
		borders[1],
	)

	def rotate(b, n):
		for _ in range(n):
			b = Borders(
				b.left[::-1],
				b.top,
				b.right[::-1],
				b.bottom,
			)
		return b

	border_options = (
		# no transform
		borders,
		# rotations
		rotate(borders, 1),
		rotate(borders, 2),
		rotate(borders, 3),
		# flipped
		flipped,
		# flipped + rotations
		rotate(flipped, 1),
		rotate(flipped, 2),
		rotate(flipped, 3),
	)
	return Tile(id, border_options)

def solve(size, fixed, candidates):
	if not candidates:
		# everything is fixed, which means we're done!
		return fixed
	for row, col in itertools.product(range(size), repeat=2):
		if (row, col) in fixed:
			# already done, move on
			continue
		# try each possible tile
		for tile in candidates:
			# try each possible arrangement
			for borders in tile.border_options:
				# check if border is allowed by looking at above and left tiles
				if (row, col - 1) in fixed and fixed[row, col-1].borders.right != borders.left:
					continue
				if (row - 1, col) in fixed and fixed[row-1, col].borders.bottom != borders.top:
					continue
				# this arrangement is allowed with what we have so far, try fixing it
				# and attempting to solve from there.
				new_fixed = fixed.copy()
				new_fixed[row, col] = FixedTile(tile.id, borders)
				result = solve(size, new_fixed, [c for c in candidates if c is not tile])
				if result:
					# it worked! we're done
					return result
				# turns out this arrangement causes problems down the line. try something else.
		# We tried everything and nothing worked. Report failure back.
		return None

tiles = map(parse_tile, sys.stdin.read().strip().split('\n\n'))
size = int(len(tiles)**0.5)
assert len(tiles) == size**2, "not a square number of tiles"
solution = solve(size, {}, tiles)
assert solution, "no solution found"

mult = 1
for corner in ((0, 0), (size - 1, 0), (0, size - 1), (size - 1, size - 1)):
	mult *= solution[corner].id
print mult
