import sys

numbers = map(int, sys.stdin.read().split(','))[::-1]

for _ in range(2020 - len(numbers)):
	try:
		ago = numbers[1:].index(numbers[0]) + 1
	except ValueError:
		ago = 0
	numbers.insert(0, ago)
	print ago
