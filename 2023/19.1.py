
import sys

workflow_input, part_input = sys.stdin.read().strip().split("\n\n")

workflows = {}
for line in workflow_input.split("\n"):
	name, rest = line.split("{")
	rule_input = rest[:-1].split(",")
	rules = []
	for rule in rule_input:
		if ":" in rule:
			rule, target = rule.split(":")
			key = rule[0]
			op = rule[1]
			threshold = int(rule[2:])
			rules.append((target, key, op, threshold))
		else:
			rules.append((rule,))
	workflows[name] = rules

parts = []
for line in part_input.split("\n"):
	part = {}
	for kv in line[1:-1].split(","):
		k, v = kv.split("=")
		part[k] = int(v)
	parts.append(part)

def process(part):
	workflow = "in"
	while workflow not in "AR":
		for rule in workflows[workflow]:
			if len(rule) == 1:
				target, = rule
				match = True
			else:
				target, key, op, threshold = rule
				match = part[key] > threshold if op == ">" else part[key] < threshold
			if match:
				workflow = target
				break
	return workflow == "A"

print sum(
	sum(part.values())
	for part in parts
	if process(part)
)
		
