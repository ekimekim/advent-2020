import sys
import re

def _parse(expr):
	# parse to list of [VALUE, OP, VALUE, OP, ...]
	parts = []
	while expr:
		char = expr[0]
		if char == '(':
			subexpr, expr = _parse(expr[1:])
			parts.append(subexpr)
		elif char == ')':
			expr = expr[1:]
			break
		elif char.isdigit():
			value, expr = re.match('^(\d+)(.*)$', expr).groups()
			value = int(value)
			parts.append(value)
		elif char in '+*':
			parts.append(char)
			expr = expr[1:]
		else:
			raise ValueError("Unknown character {!r}".format(char))
		expr = expr.strip()

	# group by '*' ops and sum each part between them
	mult_parts = []
	total = 0
	for part in parts:
		if part == '*':
			mult_parts.append(total)
			total = 0
		elif part == '+':
			pass
		else:
			total += part
	# multiply together all the grouped values
	for part in mult_parts:
		total *= part
	return total, expr

def parse(expr):
	tree, remainder = _parse(expr)
	if remainder:
		raise ValueError("Trailing data: {!r}".format(remainder))
	return tree

print sum(
	parse(line)
	for line in sys.stdin
)
