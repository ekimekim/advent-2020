
import sys
import itertools

dirs, nodes = sys.stdin.read().strip().split("\n\n")
dirs = itertools.cycle(0 if c == "L" else 1 for c in dirs)

nodes = {
	line[:3]: (line[7:10], line[12:15])
	for line in nodes.split("\n")
}

current = set(node for node in nodes if node.endswith("A"))
count = 0
while any(not node.endswith("Z") for node in current):
	dir = dirs.next()
	current = set(nodes[node][dir] for node in current)
	count += 1
	if count % 1000 == 0:
		print len([node for node in current if node.endswith("Z")]), ", ".join(current)

print count
