
import sys
import itertools

START = "AAA"
END = "ZZZ"

dirs, nodes = sys.stdin.read().strip().split("\n\n")
dirs = itertools.cycle(0 if c == "L" else 1 for c in dirs)

nodes = {
	line[:3]: (line[7:10], line[12:15])
	for line in nodes.split("\n")
}

node = START
count = 0
while node != END:
	dir = dirs.next()
	node = nodes[node][dir]
	count += 1

print count
