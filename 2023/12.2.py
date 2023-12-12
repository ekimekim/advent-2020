import sys
import re

from functools import cache

@cache
def solve(values, runs, current=0):
	run_idx = 0
	for i, c in enumerate(values):
		if c == ".":
			# end current run if any
			if current == 0:
				continue
			if run_idx >= len(runs):
				# more runs than listed, fail
				return 0
			if current != runs[run_idx]:
				# run did not match expected, fail
				return 0
			run_idx += 1
			current = 0
			continue
		if c == "#":
			# add to current run. if we weren't expecting any more runs, fail fast.
			current += 1
			if run_idx == len(runs):
				return 0
			if runs[run_idx] < current:
				return 0
			continue
		# we have an unknown. try each option.
		remaining_values = values[i+1:]
		remaining_runs = runs[run_idx:]
		return (
			solve("." + remaining_values, remaining_runs, current) +
			solve("#" + remaining_values, remaining_runs, current)
		)
	# If we made it here, we reached end of values. Check if any unmatched runs remain.
	return 1 if run_idx == len(runs) else 0

total = 0
for line in sys.stdin.read().strip().split("\n"):
	values, runs = line.split()
	runs = tuple(map(int, runs.split(",")))
	values = "?".join([values] * 5)
	# always end in a . as this is an easy way to do checks on the final run
	values += "."
	runs = runs * 5
	count = solve(values, runs)
	total += count
	print(values, ",".join(map(str, runs)), count)

print(total)
