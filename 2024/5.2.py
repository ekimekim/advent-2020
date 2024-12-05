import sys

deps, runs = sys.stdin.read().strip().split("\n\n")
deps = [line.split("|") for line in deps.split("\n")]
runs = [line.split(",") for line in runs.split("\n")]

deps_of = {}
for before, after in deps:
	deps_of.setdefault(after, []).append(before)

def topo_sort(run):
	result = []
	to_add = set(run)
	while to_add:
		for candidate in to_add:
			if any(dep in to_add for dep in deps_of[candidate]):
				continue
			result.append(candidate)
			to_add.remove(candidate)
			break
		else:
			raise ValueError("Dependency loop")
	return result

total = 0
for run in runs:
	for before, after in deps:
		if before in run and after in run and run.index(before) > run.index(after):
			run = topo_sort(run)
			total += int(run[len(run)//2])
			break

print(total)
