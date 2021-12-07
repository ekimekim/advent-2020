
import sys

positions = map(int, sys.stdin.read().strip().split(","))
# apparently the median minimises the total error, for reasons i don't understand
median = sorted(positions)[len(positions)/2]
print sum(abs(p - median) for p in positions)
