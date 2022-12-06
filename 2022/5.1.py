
import sys

stackstr, moves = sys.stdin.read().rstrip().split("\n\n")

stacks = []
for line in stackstr.split("\n")[::-1]:
	if line.startswith(" 1"):
		continue # index line
	for stack_index, str_index in enumerate(range(1, len(line), 4)):
		if len(stacks) <= stack_index:
			stacks.append([])
		if line[str_index] != " ":
			stacks[stack_index].append(line[str_index])

for move in moves.split("\n"):
	_move, num, _from, src, _to, dest = move.split()
	num = int(num)
	src = int(src) - 1
	dest = int(dest) - 1
	for _ in range(num):
		box = stacks[src].pop()
		stacks[dest].append(box)

print "".join(stack[-1] for stack in stacks)
