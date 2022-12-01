import sys
from collections import namedtuple

actions = [
	(line[0], int(line[1:]))
	for line in sys.stdin
]

State = namedtuple('State', ['x', 'y', 'wx', 'wy'])

def rotate(state, steps):
	wx, wy = state.wx, state.wy
	wx, wy = [
		(wx, wy), # none
		(wy, -wx), # left
		(-wx, -wy), # turn around
		(-wy, wx), # right
	][steps % 4]
	return state._replace(wx=wx, wy=wy)

transitions = {
	'N': lambda s, v: s._replace(wy=s.wy-v),
	'S': lambda s, v: s._replace(wy=s.wy+v),
	'E': lambda s, v: s._replace(wx=s.wx+v),
	'W': lambda s, v: s._replace(wx=s.wx-v),
	'L': lambda s, v: rotate(state, v/90),
	'R': lambda s, v: rotate(state, -v/90),
	'F': lambda s, v: s._replace(
		x = s.x + v * s.wx,
		y = s.y + v * s.wy,
	),
}

state = State(0, 0, 10, -1)
for action, value in actions:
	print state
	print action, value
	state = transitions[action](state, value)
	print state
	print

print abs(state.x) + abs(state.y)
