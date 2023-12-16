
import sys

def hash(s):
	t = 0
	for c in s:
		t = ((t + ord(c)) * 17) % 256
	return t

steps = sys.stdin.read().strip().split(",")
print("part 1", sum(map(hash, steps)))

boxes = [{} for _ in range(256)]
for step in steps:
	if step.endswith("-"):
		key = step[:-1]
		box = boxes[hash(key)]
		box.pop(key, None)
	else:
		key, value = step.split("=")
		box = boxes[hash(key)]
		box[key] = int(value)

print("part 2", sum(
	(b + 1) * (i + 1) * value
	for b, box in enumerate(boxes)
	for i, value in enumerate(box.values())
))
