
import sys
from collections import Counter

table = sys.stdin.read().strip().split('\n')

def most_common(rows, col):
	c = Counter([line[col] for line in rows])
	return '0' if c['0'] > c['1'] else '1'

oxy = table
co2 = table
for col in range(len(table[0])):
	if len(oxy) > 1:
		oxy = [line for line in oxy if line[col] == most_common(oxy, col)]
	if len(co2) > 1:
		co2 = [line for line in co2 if line[col] != most_common(co2, col)]

print int(oxy[0], 2)
print int(co2[0], 2)
print int(oxy[0], 2) * int(co2[0], 2)
