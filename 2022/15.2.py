
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

for y in range(4000000):
	x = 0
	while x < 4000000:
		for sx, sy, dist in sensors:
			xdist = dist - abs(y - sy)
			if xdist <= 0:
				# no intersection with shadow
				continue
			if abs(x - sx) > xdist:
				# x is outside of shadow, ignore
				continue
			# move x to right side of shadow
			x = sx + xdist + 1
			break
		else:
			# no intersections with shadow - we're done!
			print 4000000 * x + y
			sys.exit()
