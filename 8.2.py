import sys

instrs = [
	i.split(' ', 1) for i in
	sys.stdin.read().strip().split('\n')
]
instrs = [(i, int(a)) for i, a in instrs]

def run(instrs):
	acc = 0
	seen = set()
	ip = 0

	while ip not in seen and ip < len(instrs):
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

	return acc, ip

for n, (i, a) in enumerate(instrs):
	if i == 'acc':
		continue
	i = 'jmp' if i == 'nop' else 'nop'
	acc, ip = run(instrs[:n] + [(i, a)] + instrs[n+1:])
	if ip == len(instrs):
		print acc
