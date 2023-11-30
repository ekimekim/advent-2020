import sys

instrs = sys.stdin.read().strip().split("\n")

# value is (op, value, value) or ('literal', int) or ('digit', digit number)

regs = {k: ('literal', 0) for k in 'wxyz'}
def parse(s):
	if s in 'wxyz':
		return regs[s]
	else:
		return ('literal', int(s))

digit = 0
for instr in instrs:
	op, rest = instr.split(" ", 1)
	if op == "inp":
		regs[rest] = ('digit', digit)
		digit += 1
		continue
	a, b = rest.split()
	av = parse(a)
	bv = parse(b)
	regs[a] = (op, av, bv)

ZERO = ('literal', 0)
def simplify(node):
	if node[0] == 'literal':
		return node
	if node[0] == 'digit':
		return node
	op, a, b = node
	a = simplify(a)
	b = simplify(b)
	if op == 'mul':
		if ZERO in (a, b):
			return ZERO
	if op == 'div':
		if a == ZERO:
			return ZERO
	return node, a, b

z = simplify(regs['z'])
print z
