import sys

def parse_rule(rule):
	field, rule = rule.split(': ', 1)
	valid = set()
	for part in rule.split(' or '):
		start, end = part.split('-')
		valid |= set(range(int(start), int(end)+1))
	return field, valid

rules, yours, others = sys.stdin.read().strip().split('\n\n')
rules = map(parse_rule, rules.split('\n'))
others = [
	map(int, line.split(','))
	for line in others.split('\n')[1:]
]

total = 0
for ticket in others:
	for value in ticket:
		if any(value in valid for field, valid in rules):
			continue
		total += value

print total
