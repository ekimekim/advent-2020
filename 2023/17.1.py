
import heapq
import sys

def dist(a, b):
	return sum(abs(av - bv) for av, bv in zip(a, b))

def add(a, b):
	return tuple(av + bv for av, bv in zip(a, b))

UP, RIGHT, DOWN, LEFT = range(4)
MAX_STRAIGHTS = 3

DELTAS = {
	UP: (0, -1),
	RIGHT: (1, 0),
	DOWN: (0, 1),
	LEFT: (-1, 0),
}

costs = [map(int, line) for line in sys.stdin.read().strip().split("\n")]
width = len(costs[0])
height = len(costs)

start = 0, 0
target = width - 1, height - 1
seen = set() # set of nodes (position, direction, previous straight steps in a row)
queue = [(dist(start, target), 0, (start, RIGHT, 0))] # heap of (estimated cost, actual cost so far, node)
result = None
while queue:
	_, cost, node = heapq.heappop(queue)
	if node in seen:
		continue
	seen.add(node)
	pos, dir, straights = node
	if pos == target:
		result = cost
		break
	# try left, right and straight
	for d_dir, new_straights in [(-1, 0), (1, 0), (0, straights + 1)]:
		if new_straights >= MAX_STRAIGHTS:
			# skip node, not allowed
			continue
		new_dir = (dir + d_dir) % 4
		new_pos = add(pos, DELTAS[new_dir])
		nx, ny = new_pos
		if nx < 0 or ny < 0 or nx >= width or ny >= height:
			# skip node, hit edge
			continue
		new_cost = cost + costs[ny][nx]
		new_dist = dist(new_pos, target)
		heapq.heappush(queue, (new_cost + new_dist, new_cost, (new_pos, new_dir, new_straights)))

print result
