"""
for each monkey:
	for each item:
		worry = operation(worry) // 3
		throw according to test

throw = move to end of monkey's list
count how many inspections per monkey
"""

import sys

monkeys = []
modulus = 1
for lines in sys.stdin.read().strip().split("\n\n"):
	_, items, op, test, next_true, next_false = lines.split("\n")
	items = list(map(int, items.split(":")[1].split(", ")))
	_, _new, _equals, _old, operator, operand = op.split()
	assert operator in '*+'
	if operand != 'old':
		operand = int(operand)
	divisor = int(test.split()[-1])
	modulus *= divisor
	next_true = int(next_true.split()[-1])
	next_false = int(next_false.split()[-1])
	monkeys.append((items, operator, operand, divisor, next_true, next_false, [0]))

for round in range(10000):
	for items, operator, operand, divisor, next_true, next_false, count in monkeys:
		for item in items:
			if operator == '*':
				item *= item if operand == 'old' else operand
			else:
				item += item if operand == 'old' else operand
			item %= modulus
			if item % divisor == 0:
				next = next_true
			else:
				next = next_false
			monkeys[next][0].append(item)
			count[0] += 1
		del items[:]

a, b = sorted(monkey[-1][0] for monkey in monkeys)[-2:]
print a * b
