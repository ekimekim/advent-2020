import sys

sacks = sys.stdin.read().strip().split("\n")

def pri(c):
	return 1 + ( ord(c) - ord('a') if c.lower() == c else 26 + ord(c) - ord('A'))

wrongs = [
	list(set(sack[:len(sack)/2]) & set(sack[len(sack)/2:]))[0]
	for sack in sacks
]

print sum(map(pri, wrongs))

i = iter(sacks)
groups = zip(i, i, i)
badges = [
	list(set(group[0]).intersection(*group))[0]
	for group in groups
]
print sum(map(pri, badges))
