
import sys

x = 1
cycle = 0
result = 0
for instr in sys.stdin.read().strip().split("\n"):
	if instr == 'noop':
		new_cycle = cycle + 1
		new_x = x
	else:
		_, n = instr.split()
		new_x = x + int(n)
		new_cycle = cycle + 2
	for c in range(cycle + 1, new_cycle + 1):
		if (c - 20) % 40 == 0:
			result += c * x
	cycle = new_cycle
	x = new_x
	if cycle >= 220:
		break

print result
