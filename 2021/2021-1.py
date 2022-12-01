
import sys

depths = map(int, sys.stdin.read().strip().split('\n'))

count = 0
for prev, next in zip(depths, depths[1:]):
	if prev < next:
		count += 1

print count

count = 0
for prev, next in zip(depths, depths[3:]):
	if prev < next:
		count += 1

print count
