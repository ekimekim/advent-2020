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

# condition is a list of 14 digits, each digit is a non-empty frozenset of allowed numbers
# if a set would be empty, the whole thing is None (contradiction)
TOP = (frozenset(range(1, 10)),) * 14

def merge(a, b):
	if None in (a, b):
		return None
	ret = tuple(
		ad & bd
		for ad, bd in zip(a, b)
	)
	if frozenset() in ret:
		return None
	return ret


def solve(value, targets):
	if value[0] == 'literal':
		# literals either allow any digit, or indicate a contradiction
		if value[1] in targets:
			return TOP
		else:
			return None
	if value[0] == 'digit':
		# digit values give no information

z = regs['z']
solve(z, [0])
