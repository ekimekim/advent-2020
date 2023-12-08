
import sys
import itertools

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

def gen_ends(loop):
	start, length, ends = loop
	for loop_start in itertools.count(start, length):
		for end in ends:
			yield loop_start + end

starts = [node for node in nodes if node.endswith("A")]
loops = [find_loop(start) for start in starts]
gens = [gen_ends(loop) for loop in loops]
nexts = [next(gen) for gen in gens]
while True:
	# if they're all the same, we're done
	if len(set(nexts)) == 1:
		print nexts[0]
		break
	# otherwise, find the soonest next end (by index) and advance it
	soonest = min(range(len(nexts)), key=lambda i: nexts[i])
	nexts[soonest] = next(gens[soonest])
