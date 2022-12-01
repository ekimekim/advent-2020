import sys

input = sys.stdin.read().strip()
nums, rest = input.split("\n", 1)
nums = map(int, nums.split(','))
boards = rest.strip().split("\n\n")
boards = [
	{
		int(num): (x, y)
		for y, line in enumerate(board.split("\n"))
		for x, num in enumerate(line.strip().split())
	} for board in boards
]

class Done(Exception):
	pass

found = [set() for _ in boards]
won = set()
last_won = None
last_num = None
for num in nums:
	for i, board in enumerate(boards):
		if i in won:
			continue
		if num in board:
			fb = found[i]
			fb.add(board[num])
			for x in range(5):
				if all((x, y) in fb for y in range(5)):
					last_won = i
					won.add(i)
					last_num = num
			for y in range(5):
				if all((x, y) in fb for x in range(5)):
					last_won = i
					won.add(i)
					last_num = num
print "board", last_won
print "last", last_num
s = sum([
	n
	for (n, coord) in boards[last_won].items()
	if coord not in found[last_won]
])
print s * last_num
