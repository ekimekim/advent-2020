
import sys

positions = map(int, sys.stdin.read().strip().split(","))
print min(
	sum(
		abs(pos - p) * (abs(pos - p) + 1) / 2
		for p in positions
	) for pos in range(min(positions), max(positions)+1)
)
