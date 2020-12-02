import sys
from collections import Counter

valid = 0
for line in sys.stdin:
	line = line[:-1]
	policy, password = line.split(': ', 1)
	part, char = policy.split(' ')
	positions = map(int, part.split('-'))
	if len(filter(None, [password[p-1] == char for p in positions])) == 1:
		valid += 1

print valid
