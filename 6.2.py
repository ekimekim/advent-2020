import sys

print sum(
	len(set(group.split('\n')[0]).intersection(*[
		line for line in group.split('\n')
	]))
	for group in sys.stdin.read().strip().split('\n\n')
)
