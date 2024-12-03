import sys
import re

results = []
enabled = True

def f(m):
	global enabled
	if m.group(0) == "do()":
		enabled = True
	elif m.group(0) == "don't()":
		enabled = False
	elif enabled:
		results.append(int(m.group(1)) * int(m.group(2)))

re.sub(
	r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)",
	f,
	sys.stdin.read(),
)
print(sum(results))
