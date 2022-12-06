import sys

window = ''
for i, c in enumerate(sys.stdin.read().rstrip()):
	window += c
	if len(window) < 4:
		continue
	window = window[-4:]
	if len(set(window)) == len(window):
		print i + 1
		break
