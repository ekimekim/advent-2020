import sys
from itertools import product

lines = sys.stdin.read().strip().split("\n")

gears = {}

total = 0
for y, line in enumerate(lines):
	num = ""
	nx = 0
	for x, c in enumerate(line + "."):
		if c.isdigit():
			if not num:
				nx = x
			num += c
			continue
		part = False
		for l in range(len(num)):
			for dx, dy in product((-1, 0, 1), (-1, 0, 1)):
				cy = y + dy
				cx = nx + l + dx
				if cy < 0 or cx < 0 or cy >= len(lines) or cx >= len(lines[0]):
					continue
				if lines[cy][cx] not in "0123456789.":
					if lines[cy][cx] == "*":
						gears.setdefault((cx, cy), {})[nx, y] = int(num)
					part = True
		print num, nx, part
		if part:
			total += int(num)
		num = ""

print total
print gears
print sum(nums.values()[0] * nums.values()[1] for nums in gears.values() if len(nums) == 2)
