import sys

window = ''
for i, c in enumerate(sys.stdin.read().rstrip()):
	window += c
	if len(window) < 14:
		continue
	window = window[-14:]
	if len(set(window)) == len(window):
		print i + 1
		break
