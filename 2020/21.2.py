import sys

def parse(line):
	ingredients, allergens = line.split("(contains ")
	ingredients = set(ingredients.split())
	allergens = allergens.strip()[:-1].split(", ")
	return ingredients, allergens

foods = map(parse, sys.stdin)

ingredient_for_allergen = {}
for ingredients, allergens in foods:
	for allergen in allergens:
		ingredient_for_allergen.setdefault(allergen, ingredients.copy()).intersection_update(ingredients)

known = {}
prev_known = None
while known != prev_known:
	prev_known = known
	known = {
		list(ingredients)[0]: allergen
		for allergen, ingredients in ingredient_for_allergen.items()
		if len(ingredients) == 1
	}
	for allergen, ingredients in ingredient_for_allergen.items():
		ingredients -= set(i for i, a in known.items() if a != allergen)

print ",".join(sorted(known.keys(), key=lambda i: known[i]))
