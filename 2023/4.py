import sys

lines = sys.stdin.read().strip().split("\n")

results = {}
for line in lines:
	card, numbers = line.split(": ")
	_, card = card.split()
	card = int(card)
	wins, mine = numbers.split(" | ")
	wins = set(map(int, wins.split()))
	mine = set(map(int, mine.split()))
	results[card] = len(mine & wins)

print sum([2**(wins - 1) for wins in results.values() if wins > 0])

won = 0
cards = list(results.items())
while cards:
	id, wins = cards.pop()
	won += 1
	for n in range(wins):
		cards.append((id + n + 1, results[id + n + 1]))

print won
