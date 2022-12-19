
from pprint import pprint
import sys

START_VALVE = "AA"

valves = {}
for line in sys.stdin.read().strip().split("\n"):
	valve = line.split()[1]
	rate = int(line.split("=")[1].split(";")[0])
	paths = line.split(" ", 9)[-1].split(", ")
	valves[valve] = rate, paths

#pprint(valves)

# Simplified graph {valve: {other valve: total cost to walk there and turn it on}},
# from every non-zero valve (or the start valve) to every other non-zero valve.
# We populate this with BFS from each start node.
costs = {}
nonzero_valves = [valve for valve, (rate, paths) in valves.items() if rate > 0]
for start in nonzero_valves + [START_VALVE]:
	visited = set()
	to_visit = [(start, 0)]
	while to_visit:
		valve, cost = to_visit.pop(0)
		rate, paths = valves[valve]
		if valve in visited:
			continue
		visited.add(valve)
		if rate > 0 and valve != start:
			costs.setdefault(start, {})[valve] = cost + 1
		for path in paths:
			to_visit.append((path, cost + 1))

assert set(costs.keys()) == set(nonzero_valves + [START_VALVE])
assert all(set(costs[v].keys()) == set(nonzero_valves) - {v} for v in nonzero_valves)
#pprint(costs)

# in this smaller graph, try all paths up to time limit.
def find_paths(path, score, time_left, ignore=()):
	here = path[-1]
	rate, _ = valves[here]
	score += rate * time_left
	found_any = False
	yield path, score
	for valve, cost in costs[here].items():
		if cost < time_left and valve not in path and valve not in ignore:
			found_any = True
			for result in find_paths(path + (valve,), score, time_left - cost, ignore):
				yield result

paths = list(find_paths((START_VALVE,), 0, 26))
best = (), (), 0
for i, (path, score) in enumerate(paths):
	if i % 10 == 0:
		print "{}/{} ({:.2f}%)".format(i, len(paths), 100. * i / len(paths))
	for other_path, total_score in find_paths((START_VALVE,), score, 26, path):
		if total_score > best[-1]:
			best = path, other_path, total_score
			print "New best:", best

print "Final best:", best
