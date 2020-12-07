import sys

print sum(
	len(set().union(*[
		line for line in group.split('\n')
	]))
	for group in sys.stdin.read().strip().split('\n\n')
)
