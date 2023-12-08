
import sys
import itertools
import math

dirs, nodes = sys.stdin.read().strip().split("\n\n")
dirs = [0 if c == "L" else 1 for c in dirs]

nodes = {
	line[:3]: (line[7:10], line[12:15])
	for line in nodes.split("\n")
}

def find_loop(node):
	# returns steps to start of loop, loop length, list of step counts within loop where we're at end
	states = {} # (node, dirpos): step
	ends = set() # step counts
	dirpos = 0
	for step in itertools.count():
		if node.endswith("Z"):
			ends.add(step)
		if (node, dirpos) in states:
			start_at = states[node, dirpos]
			looplen = step - start_at
			ends = [end - start_at for end in ends]
			return start_at, looplen, ends
		states[node, dirpos] = step
		dir = dirs[dirpos]
		node = nodes[node][dir]
		dirpos = (dirpos + 1) % len(dirs)

starts = [node for node in nodes if node.endswith("A")]
loops = [find_loop(start) for start in starts]
for start, loop in zip(starts, loops):
	print(start, loop)

# Simplify out loop lead-in time by rotating the loops to start at the same point
start_at = max(start for start, length, ends in loops)
new_loops = []
for start, length, ends in loops:
	rotate_by = start_at - start
	ends = [(end - rotate_by) % length for end in ends]
	new_loops.append((length, ends))
loops = new_loops

# The input seems to always have the ends be at a multiple of the loop length in terms of total
# steps. Validate this and we can simplify out the end points.
for length, ends in loops:
	assert len(ends) == 1
	end = ends[0]
	assert end + start_at == length
loops = [length for length, ends in loops]

print(math.lcm(*loops))
