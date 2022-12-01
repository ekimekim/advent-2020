
import sys

input = [
	sum(map(int, part.split("\n")))
	for part in sys.stdin.read().strip().split("\n\n")
]

print "part 1"
print max(input)

print "part 2"
print sum(sorted(input, reverse=True)[:3])
