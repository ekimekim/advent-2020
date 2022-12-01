import sys

instrs = [
	i.split(' ', 1) for i in
	sys.stdin.read().strip().split('\n')
]
instrs = [(i, int(a)) for i, a in instrs]

acc = 0
seen = set()
ip = 0

while True:
	i, a = instrs[ip]
	seen.add(ip)
	if i == 'acc':
		acc += a
		ip += 1
	elif i == 'nop':
		ip += 1
	elif i == 'jmp':
		ip += a
	else:
		assert False
	if ip in seen:
		print acc
		break
