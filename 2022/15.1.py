
import sys, re

sensors = [] # x, y, distance to nearest beacon
beacons = set()
for line in sys.stdin.read().strip().split("\n"):
	x, y, bx, by = map(int, re.findall("-?\d+", line))
	beacons.add((bx, by))
	dist = abs(x - bx) + abs(y - by)
	sensors.append((x, y, dist))

xs = [x + d for x, y, d in sensors] + [x - d for x, y, d in sensors] + [x for x, y in beacons]
ys = [y + d for x, y, d in sensors] + [y - d for x, y, d in sensors] + [y for x, y in beacons]

y = 2000000
count = 0
for x in range(min(xs), max(xs) + 1):
	if (x, y) not in beacons and any(
		abs(x - sx) + abs(y - sy) <= dist
		for sx, sy, dist in sensors
	):
		count += 1

print count
