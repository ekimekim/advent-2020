
import sys

positions = map(int, sys.stdin.read().strip().split(","))

def f(pos):
	return sum(
		abs(pos - p) * (abs(pos - p) + 1) / 2
		for p in positions
	)

pos = sum(positions) / len(positions)
error = f(pos)
new_error = f(pos + 1)
if new_error < error:
	error = new_error
	dir = 1
else:
	dir = -1
while new_error <= error:
	pos += dir
	error = new_error
	new_error = f(pos)
print error
