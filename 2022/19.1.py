import sys

RESOURCES = ["ore", "clay", "obsidian", "geodes"]

blueprints = []
for line in sys.stdin.read().strip().split("\n"):
	recipes = []
	for recipe in line.split(": ")[1].rstrip(".").split(". "):
		costs = [0, 0, 0]
		for part in recipe.split(" costs ")[1].split(" and "):
			n, resource = part.split()
			n = int(n)
			costs[RESOURCES.index(resource)] = n
		recipes.append(tuple(costs))
	assert len(recipes) == 4
	blueprints.append(recipes)

def find_best(memo, current, production, time_left):
