
import sys
from collections import Counter

table = sys.stdin.read().strip().split('\n')

gamma = ''
for col in range(len(table[0])):
	gamma += Counter([line[col] for line in table]).most_common(1)[0][0]

gamma = int(gamma, 2)
epsilon = ((1 << len(table[0])) - 1) & ~gamma
print gamma * epsilon
