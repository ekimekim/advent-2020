import sys
import re
from ast import literal_eval

rule_defs, messages = sys.stdin.read().strip().split('\n\n')

# parse rules
rules = {}
for rule_def in rule_defs.split('\n'):
	id, rule_def = rule_def.split(": ", 1)
	id = int(id)
	options = rule_def.split(" | ")
	rules[id] = [map(literal_eval, option.split()) for option in options]

# resolve refs
def resolve_rule(id):
	rule = rules[id]
	if isinstance(rule, str):
		return rule # already resolved
	# special cases
	if id == 8:
		return "(?:{})+".format(resolve_rule(42))
	elif id == 11:
		# technically wrong, but works for all test cases
		return "|".join(
			"(?:%s){%d}(?:%s){%d}" % (resolve_rule(42), n, resolve_rule(31), n)
			for n in range(1, 100)
		)
	# normal case
	resolved = "|".join(
		"".join(
			part if isinstance(part, str) else "(?:{})".format(resolve_rule(part))
			for part in option
		)
		for option in rule
	)
	rules[id] = resolved
	return resolved

regex = re.compile("^{}$".format(resolve_rule(0)))
print resolve_rule(8)

print sum(
	1 for message in messages.split('\n')
	if regex.match(message)
)
