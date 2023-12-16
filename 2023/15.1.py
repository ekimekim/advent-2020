
import sys

def hash(s):
	t = 0
	for c in s:
		t = ((t + ord(c)) * 17) % 256
	return t

steps = sys.stdin.read().strip().split(",")
print "part 1", sum(map(hash, steps))

boxes = [[] for _ in range(256)]
for step in steps:
	if step.endswith("-"):
		key = step[:-1]
		box = boxes[hash(key)]
		boxes[hash(key)] = [(k, v) for k, v in box if k != key]
	else:
		key, value = step.split("=")
		box = boxes[hash(key)]
		for i, (k, v) in enumerate(box):
			if k == key:
				box[i] = key, value
				break
		else:
			box.insert((key, value), 0)
