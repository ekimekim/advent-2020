import sys

deps, runs = sys.stdin.read().strip().split("\n\n")
deps = [line.split("|") for line in deps.split("\n")]
runs = [line.split(",") for line in runs.split("\n")]

total = 0
for run in runs:
	for before, after in deps:
		if before in run and after in run and run.index(before) > run.index(after):
			break
	else:
		total += int(run[len(run)//2])

print(total)
