import sys
from collections import namedtuple

actions = [
	(line[0], int(line[1:]))
	for line in sys.stdin
]

State = namedtuple('State', ['x', 'y', 'facing'])

transitions = {
	'N': lambda s, v: s._replace(y=s.y-v),
	'S': lambda s, v: s._replace(y=s.y+v),
	'E': lambda s, v: s._replace(x=s.x+v),
	'W': lambda s, v: s._replace(x=s.x-v),
	'L': lambda s, v: s._replace(facing=(s.facing-(v/90)) % 4),
	'R': lambda s, v: s._replace(facing=(s.facing+(v/90)) % 4),
	'F': lambda s, v: s._replace(
		x = s.x + [0, v, 0, -v][s.facing],
		y = s.y + [-v, 0, v, 0][s.facing],
	),
}

state = State(0, 0, 1)
for action, value in actions:
	state = transitions[action](state, value)

print abs(state.x) + abs(state.y)
