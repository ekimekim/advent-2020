import sys

def parse_rule(rule):
	field, rule = rule.split(': ', 1)
	valid = set()
	for part in rule.split(' or '):
		start, end = part.split('-')
		valid |= set(range(int(start), int(end)+1))
	return field, valid

rules, yours, others = sys.stdin.read().strip().split('\n\n')
rules = dict(map(parse_rule, rules.split('\n')))
yours = map(int, yours.split('\n')[1].split(','))
others = [
	map(int, line.split(','))
	for line in others.split('\n')[1:]
]

# filter out invalid tickets
others = [
	ticket for ticket in others
	if all(
		any(value in valid for valid in rules.values())
		for value in ticket
	)
]

field_map = {
	index: rules.keys()
	for index in range(len(yours))
}

# eliminate fields based on invalid values
for ticket in [yours] + others:
	for index, value in enumerate(ticket):
		# filter out any fields where this value would be wrong
		field_map[index] = [
			field for field in field_map[index]
			if value in rules[field]
		]
		assert field_map[index], "no options left for index {}".format(index)

# eliminate fields because we know they must go elsewhere
prev_field_map = None
while field_map != prev_field_map:
	known = {fields[0]: index for index, fields in field_map.items() if len(fields) == 1}
	prev_field_map = field_map
	field_map = {
		index: [
			field for field in fields
			if field not in known or known[field] == index
		]
		for index, fields in field_map.items()
	}

assert all(len(v) == 1 for v in field_map.values()), "no unique solution: {}".format(field_map)

mult = 1
for index, fields in field_map.items():
	if not fields[0].startswith("departure "):
		continue
	mult *= yours[index]

print mult
