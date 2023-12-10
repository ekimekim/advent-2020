import sys

lines = sys.stdin.read().strip().split("\n")
lines = [map(int, line.split()) for line in lines]

def predict(values):
	diffs = [b - a for a, b in zip(values, values[1:])]
	if set(diffs) == {0}:
		d_next = 0
	else:
		d_next = predict(diffs)
	return values[-1] + d_next

print sum(predict(values) for values in lines)
