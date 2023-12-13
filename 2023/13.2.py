import sys

sections = sys.stdin.read().strip().split("\n\n")

total = 0
for grid in sections:
	grid = grid.split("\n")
	for y in range(1, len(grid)):
		if sum(
			1 if ac != bc else 0
			for a, b in zip(
				grid[y:],
				grid[:y][::-1],
			)
			for ac, bc in zip(a, b)
		) == 1:
			total += 100 * y
			print "y =", y
			break
	else:
		for x in range(1, len(grid[0])):
			if sum(
				1 if ac != bc else 0
				for y in range(len(grid))
				for ac, bc in zip(grid[y][x:], grid[y][:x][::-1])
			) == 1:
				total += x
				print "x =", x
				break
		else:
			print "No match"
			print "\n".join(grid)
			assert False

print total
