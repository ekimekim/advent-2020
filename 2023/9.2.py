import sys

lines = sys.stdin.read().strip().split("\n")
lines = [map(int, line.split()) for line in lines]

def predict(values):
	diffs = [b - a for a, b in zip(values, values[1:])]
	if set(diffs) == {0}:
		d_prev = 0
	else:
		d_prev = predict(diffs)
	return values[0] - d_prev

print sum(predict(values) for values in lines)
