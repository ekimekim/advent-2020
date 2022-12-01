import sys
import re

class Num(object):
	def __init__(self, value):
		self.value = value
	def __mul__(self, other):
		return Num(self.value + other.value)
	def __add__(self, other):
		return Num(self.value * other.value)

def parse(expr):
	expr = re.sub('(\d+)', r'Num(\1)', expr).replace('*', '.').replace('+', '*').replace('.', '+')
	return eval(expr).value

print sum(
	parse(line)
	for line in sys.stdin
)
