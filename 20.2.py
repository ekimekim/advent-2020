
import itertools
import sys
import re
from collections import namedtuple, Counter

Tile = namedtuple('Tile', ['id', 'data_options', 'border_options'])
FixedTile = namedtuple('FixedTile', ['id', 'data', 'borders'])
Borders = namedtuple('Borders', ['top', 'right', 'bottom', 'left'])

def rotate(data):
	return [
		"".join(
			data[-x-1][y]
			for x in range(len(data))
		) for y in range(len(data))
	]

def rotate_n(data, n):
	for _ in range(n):
		data = rotate(data)
	return data

def parse_tile(tile):
	id = int(tile.split('\n')[0].split()[1][:-1])
	data = tile.split('\n')[1:]

	def data_to_borders(data):
		return Borders(
			data[0],
			"".join(row[-1] for row in data),
			data[-1],
			"".join(row[0] for row in data),
		)

	# this is a vertical flip
	flipped = data[::-1]

	data_options = (
		# no transform
		data,
		# rotations
		rotate_n(data, 1),
		rotate_n(data, 2),
		rotate_n(data, 3),
		# flipped
		flipped,
		# flipped + rotations
		rotate_n(flipped, 1),
		rotate_n(flipped, 2),
		rotate_n(flipped, 3),
	)
	border_options = tuple(map(data_to_borders, data_options))
	return Tile(id, data_options, border_options)

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
			for data, borders in zip(tile.data_options, tile.border_options):
				# check if border is allowed by looking at above and left tiles
				if (row, col - 1) in fixed and fixed[row, col-1].borders.right != borders.left:
					continue
				if (row - 1, col) in fixed and fixed[row-1, col].borders.bottom != borders.top:
					continue
				# this arrangement is allowed with what we have so far, try fixing it
				# and attempting to solve from there.
				new_fixed = fixed.copy()
				new_fixed[row, col] = FixedTile(tile.id, data, borders)
				result = solve(size, new_fixed, [c for c in candidates if c is not tile])
				if result:
					# it worked! we're done
					return result
				# turns out this arrangement causes problems down the line. try something else.
		# We tried everything and nothing worked. Report failure back.
		return None

tiles = map(parse_tile, sys.stdin.read().strip().split('\n\n'))
tile_size = len(tiles[0].data_options[0])
size = int(len(tiles)**0.5)
assert len(tiles) == size**2, "not a square number of tiles"
solution = solve(size, {}, tiles)
assert solution, "no solution found"

data = [
	"".join(
		solution[row, col].data[subrow][1:-1]
		for col in range(size)
	)
	for row in range(size)
	for subrow in range(1, tile_size - 1)
]

def find_monsters(data):
	monster_re = (".{%d}" % (len(data) - 20)).join([
		                  "#.",
		"#....##....##....###",
		".#..#..#..#..#..#",
	])
	return len(re.findall(monster_re, "".join(data)))

flipped = data[::-1]
monsters = max(find_monsters(d) for d in [
	# no transform
	data,
	# rotations
	rotate_n(data, 1),
	rotate_n(data, 2),
	rotate_n(data, 3),
	# flipped
	flipped,
	# flipped + rotations
	rotate_n(flipped, 1),
	rotate_n(flipped, 2),
])

print monsters, Counter("".join(data))['#'] - 15 * monsters
