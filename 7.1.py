
import sys
import re


def parse(line):
	# returns (outer bag, [(number, inner bag)])
	line = line.rstrip('.')
	target, contents = line.split(' bags contain ', 1)
	if contents == 'no other bags':
		contents = []
	else:
		contents = map(parse_content, contents.split(', '))
	return target, contents


def parse_content(content):
	n, rest = content.split(' ', 1)
	if rest.endswith(' bag'):
		rest = rest[:-4]
	else:
		# bags
		rest = rest[:-5]
	return int(n), rest


# {outer: [(n, inner)]}
rules = dict(map(parse, sys.stdin.read().strip().split('\n')))
print rules

reasons = {}

def can_have_ours(color):
	if color == 'shiny gold':
		reasons[color] = (color,)
		return True
	for n, child in rules[color]:
		if can_have_ours(child):
			reasons[color] = (color,) + reasons[child]
			print color, "can contain because", reasons[color]
			return True
	return False

n = 0
for color in rules:
	if can_have_ours(color):
		n += 1
print n
