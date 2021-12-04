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
try:
	for num in nums:
		for i, board in enumerate(boards):
			if num in board:
				fb = found[i]
				fb.add(board[num])
				for x in range(5):
					if all((x, y) in fb for y in range(5)):
						raise Done(i)
				for y in range(5):
					if all((x, y) in fb for x in range(5)):
						raise Done(i)
except Done as d:
	i, = d.args
	print "board", i
	print sum([
		n
		for (n, coord) in boards[i].items()
		if coord not in fb
	]) * num
else:
	print "failed"
