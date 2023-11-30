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

def simplify(node):
	if node[0] == 'literal':
		return node
	if node[0] == 'digit':
		return node
	op, a, b = node
	a = simplify(a)
	b = simplify(b)
	al = a[1] if a[0] == 'literal' else None
	bl = b[1] if b[0] == 'literal' else None
	if op == 'mul':
		if al == 0 or bl == 0:
			return ('literal', 0)
	if op == 'div':
		if al == 0:
			return 

print regs['z']
