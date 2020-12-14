import sys

to_set = 0
to_keep = 0
mem = {}

for line in sys.stdin:
	dest, value = line.split(' = ')
	if dest == 'mask':
		# force Xs to 0s (don't set)
		to_set = int(value.replace('X', '0'), 2)
		# force Xs to 1s (keep)
		to_keep = int(value.replace('X', '1'), 2)
	else:
		addr = dest[4:-1] # strip "mem[" and "]"
		value = (int(value) | to_set) & to_keep
		mem[addr] = value

print sum(mem.values())
