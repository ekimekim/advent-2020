import sys
from collections import Counter

valid = 0
for line in sys.stdin:
	line = line[:-1]
	policy, password = line.split(':', 1)
	part, char = policy.split(' ')
	least, most = map(int, part.split('-'))
	counts = Counter(password)
	if least <= counts.get(char, 0) <= most:
		valid += 1

print valid
