import sys
import re

def _parse(expr):
	tree = (lambda _, y: y, 0)
	# we have two transforms to tree: a value or an operator (subexpressions are values):
	#  op: tree -> (op, tree)
	#  value: (op, value) -> (op, value, value)
	# to handle the special first-value case, we have an identity op with 0 for lhs.
	while expr:
		char = expr[0]
		if char == '(':
			value, expr = _parse(expr[1:])
			tree += (value,)
		elif char == ')':
			expr = expr[1:]
			break
		elif char.isdigit():
			value, expr = re.match('^(\d+)(.*)$', expr).groups()
			value = int(value)
			tree += (value,)
		elif char == '+':
			tree = (lambda x, y: x + y, tree)
			expr = expr[1:]
		elif char == '*':
			tree = (lambda x, y: x * y, tree)
			expr = expr[1:]
		else:
			raise ValueError("Unknown character {!r}".format(char))
		expr = expr.strip()
	return tree, expr

def parse(expr):
	tree, remainder = _parse(expr)
	if remainder:
		raise ValueError("Trailing data: {!r}".format(remainder))
	return tree

def run(tree):
	if isinstance(tree, int):
		return tree
	op, x, y = tree
	return op(run(x), run(y))

print sum(
	run(parse(line))
	for line in sys.stdin
)
