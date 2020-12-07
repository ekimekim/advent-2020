
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

def count(color):
	return 1 + sum(n * count(child) for n, child in rules[color])

print count('shiny gold') - 1 # don't count outermost bag
