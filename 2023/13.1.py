import sys

sections = sys.stdin.read().strip().split("\n\n")

total = 0
for grid in sections:
	grid = grid.split("\n")
	for y in range(1, len(grid)):
		if all(
			a == b
			for a, b in zip(
				grid[y:],
				grid[:y][::-1],
			)
		):
			total += 100 * y
			print "y =", y
			break
	else:
		for x in range(1, len(grid[0])):
			rlen = min(x, len(grid[0]) - x)
			if all(
				grid[y][x:][:rlen] == grid[y][:x][::-1][:rlen]
				for y in range(len(grid))
			):
				total += x
				print "x =", x
				break
		else:
			print "No match"
			print "\n".join(grid)
			assert False

print total
