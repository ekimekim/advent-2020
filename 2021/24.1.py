import sys
import math

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

def is_eql(parts):
	if len(parts) != 1: return False
	scalar, bases = parts[0]
	if scalar != 1: return False
	if len(bases) != 1: return False
	return bases[0][0] == 'eql'

def str_value(parts):
	if parts == ():
		return "0"
	return " + ".join(map(str_part, parts))

def str_part((scalar, bases)):
	if not bases:
		return str(scalar)
	bases_str = "*".join(map(str_base, bases))
	if scalar == 1:
		return bases_str
	return "{}*{}".format(scalar, bases_str)

def str_base(base):
	if base[0] == "digit":
		return "${}".format(base[1])
	op, a, b = base
	sym = {
		'eql': '==',
		'neq': '!=',
		'mod': '%',
		'div': '/',
	}[op]
	return "({} {} {})".format(str_value(a), sym, str_value(b))

def possible(parts):
	# returns a set of possible values for value
	def by_element(a, b, f):
		return set(f(x, y) for x in a for y in b)

	result = {0}
	for scalar, bases in parts:
		possible_part = {scalar}
		for base in bases:
			if base[0] == 'digit':
				possible_base = set(range(1, 10))
			else:
				op, a, b = base
				op = {
					'eql': lambda x, y: 1 if x == y else 0,
					'neq': lambda x, y: 0 if x == y else 1,
					'mod': lambda x, y: x % y,
					'div': lambda x, y: math.trunc(float(x) / y),
				}[op]
				possible_base = by_element(possible(a), possible(b), op)
			possible_part = by_element(possible_part, possible_base, lambda x, y: x * y)
		result = by_element(result, possible_part, lambda x, y: x + y)
	return result

regs = {k: () for k in 'wxyz'}
def parse(s):
	if s in 'wxyz':
		return regs[s]
	else:
		return scalar(int(s))

ZERO = ()
ONE = scalar(1)

index = 0
for instr in instrs:
	print instr
	op, rest = instr.split(" ", 1)
	if op == "inp":
		regs[rest] = digit(index)
		print "{} = {}".format(rest, str_value(regs[rest]))
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
	elif op == 'mod' and av == ZERO:
		# 0 % x = 0
		new = ZERO
	elif op == 'div' and av == ZERO:
		# 0 / x = 0
		new = ZERO
	elif op == 'div' and bv == ONE:
		# x / 1 = x
		new = av
	elif op == 'eql' and av == bv:
		# not likely, but if the two sides are symbolically equal they MUST be equal
		# note the inverse is not true
		new = ONE
	elif op == 'eql' and ONE in (av, bv):
		# x == 1 is equivalent to x
		new = av if bv == ONE else bv
	elif op == 'eql' and is_eql(av) and bv == ZERO:
		# eql(a, b) == 0 means a != b, we special case this as its own operator
		_, inner_a, inner_b = av[0][1][0]
		new = wrap('neq', inner_a, inner_b)
	elif op == 'eql':
		ap = possible(av)
		bp = possible(bv)
		if not (ap & bp):
			new = ZERO
		elif ap == bp and len(ap) == 1:
			new = ONE
		else:
			if len(ap) == 1: av = scalar(list(ap)[0])
			if len(bp) == 1: bv = scalar(list(bp)[0])
			new = wrap(op, av, bv)
	else:
		# we can't do anything sensible here
		new = wrap(op, av, bv)

	new = simplify(new)
	regs[a] = new
	print "{} = {}".format(a, str_value(new))
