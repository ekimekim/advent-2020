import sys

instrs = sys.stdin.read().strip().split("\n")

# value is a list of parts
# each part is (scalar, bases)
# bases is a list of ('digit', index) or (op, value, value)
# part value = scalar * product(bases)
# total value = sum(parts)

def scalar(value):
	if value == 0:
		return ()
	# scalar has no bases
	return ((value, ()),)

def digit(index):
	# scale of 1, single base
	return ((1, (('digit', index),)),)

def wrap(op, a, b):
	# scale of 1, base = the wrapped op
	return ((1, ((op, a, b),)),)

def simplify(parts):
	# find any common bases and combine them
	result = []
	for scalar, bases in parts:
		found = False
		for i, (s, b) in enumerate(result):
			if bases == b:
				result[i] = (scalar + s, bases)
				found = True
		if not found:
			result.append((scalar, bases))
	result = [(s, b) for s, b in result if s != 0]
	return tuple(sorted(result))

regs = {k: () for k in 'wxyz'}
def parse(s):
	if s in 'wxyz':
		return regs[s]
	else:
		return scalar(int(s))

index = 0
for instr in instrs:
	op, rest = instr.split(" ", 1)
	if op == "inp":
		regs[rest] = digit(index)
		index += 1
		continue
	a, b = rest.split()
	av = parse(a)
	bv = parse(b)

	if op == 'add':
		# just combine the parts and simplify
		new = av + bv
	elif op == 'mul':
		# multiply every base from A with every base from B,
		# ie. (ax + by)(cw + dz) = acxw + adxz + bcyw + bdyz
		result = []
		for a_s, a_b in av:
			for b_s, b_b in bv:
				result.append((a_s * b_s, tuple(sorted(a_b + b_b))))
		new = tuple(result)
	elif op == 'mod' and av == ():
		# 0 mod anything is 0
		new = ()
	elif op == 'eql' and av == bv:
		# not likely, but if the two sides are symbolically equal they MUST be equal
		# note the inverse is not true
		new = scalar(1)
	else:
		# we can't do anything sensible here
		new = wrap(op, av, bv)

	print op, av, bv, "->", new
	regs[a] = simplify(new)

print regs['z']
