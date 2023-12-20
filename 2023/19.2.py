
from collections import namedtuple
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

Part = namedtuple("Part", ["x", "m", "a", "s"])

ALL_PARTS = Part((1, 4001), (1, 4001), (1, 4001), (1, 4001))

queue = [("in", ALL_PARTS)]
accepted = []
while queue:
	workflow, part = queue.pop()
	if workflow == "A":
		accepted.append(part)
		continue
	if workflow == "R":
		continue
	for rule in workflows[workflow]:
		if len(rule) == 1:
			# unconditional rule, part is unmodified but gets new workflow
			target, = rule
			queue.append((target, part))
			break
		target, key, op, threshold = rule
		start, end = getattr(part, key)
		# conditional rule, split key range for part
		if op == ">":
			no_match = start, min(end, threshold + 1)
			match = max(start, threshold + 1), end
		else:
			match = start, min(end, threshold)
			no_match = max(start, threshold), end
		# if match range non-empty, enqueue for the new workflow
		if match[1] - match[0] > 0:
			new_part = part._replace(**{key: match})
			queue.append((target, new_part))
		# if non-match range is empty, stop this workflow. otherwise keep going
		# with new range for key.
		if no_match[1] - no_match[0] <= 0:
			break
		part = part._replace(**{key: no_match})

total = 0
for part in accepted:
	combinations = 1
	for key in "xmas":
		start, end = getattr(part, key)
		combinations *= end - start
	total += combinations

print total
