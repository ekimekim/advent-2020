import sys
import math

instrs = sys.stdin.read().strip().split("\n")

# value is (op, value, value) or ('literal', int) or ('digit', digit number)

regs = {k: {0} for k in 'wxyz'}
def parse(s):
	if s in 'wxyz':
		return regs[s]
	else:
		return {int(s)}

for instr in instrs:
	op, rest = instr.split(" ", 1)
	if op == "inp":
		regs[rest] = set(range(1, 10))
		continue
	a, b = rest.split()
	av = parse(a)
	bv = parse(b)
	opf = {
		'add': lambda a, b: a + b,
		'mul': lambda a, b: a * b,
		'div': lambda a, b: math.trunc(float(a) / b),
		'mod': lambda a, b: a % b,
		'eql': lambda a, b: 1 if a == b else 0,
	}[op]
	regs[a] = set([
		opf(x, y)
		for x in av
		for y in bv
	])

print regs['z']
