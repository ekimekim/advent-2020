import sys
import re

results = []
re.sub(
	r"mul\((\d{1,3}),(\d{1,3})\)",
	lambda m: results.append(int(m.group(1)) * int(m.group(2))),
	sys.stdin.read(),
)
print(sum(results))
