
import math
import sys
from collections import namedtuple

Module = namedtuple("Module", ["type", "outputs", "state"])

modules = {}
for line in sys.stdin.read().strip().split("\n"):
	name, outputs = line.split(" -> ")
	outputs = outputs.split(", ")
	if name == "broadcaster":
		type = "b"
		state = None
	else:
		type = name[0]
		name = name[1:]
		state = {} if type == "&" else [False]
	modules[name] = Module(type, outputs, state)

for name, module in modules.items():
	for output_name in module.outputs:
		if output_name not in modules:
			continue
		output = modules[output_name]
		if output.type == "&":
			output.state[name] = False

def run(modules, start_module, start_signal, output_module):
	queue = [("start", start_module, start_signal)] # (source, dest, is_high)
	while queue:
		source, name, is_high = queue.pop(0)
		if name == output_module:
			yield is_high
		if name not in modules:
			continue
		module = modules[name]
		if module.type == "b":
			for output in module.outputs:
				queue.append((name, output, is_high))
		elif module.type == "%":
			if not is_high:
				module.state[0] = not module.state[0]
				for output in module.outputs:
					queue.append((name, output, module.state[0]))
		elif module.type == "&":
			module.state[source] = is_high
			result = not all(module.state.values())
			for output in module.outputs:
				queue.append((name, output, result))
		else:
			assert False

def graph(modules):
	for name, module in modules.items():
		color = {"%": "green", "&": "blue"}.get(module.type, "black")
		print("[ %s ] { color: %s; }" % (name, color))
		for output in module.outputs:
			print("[ %s ] -> [ %s ]" % (name, output))

def split_graph(modules):
	# Looking at the input, it is divided into subgraphs that all take input from
	# broadcaster and give output to the node before rx.
	pre_rx = [name for name, module in modules.items() if "rx" in module.outputs]
	if len(pre_rx) != 1:
		raise ValueError("Unexpected graph shape")
	pre_rx = pre_rx[0]
	subgraphs = []
	for initial in modules["broadcaster"].outputs:
		subgraph = {
			"in": Module("b", [initial], None),
		}
		queue = [initial]
		while queue:
			name = queue.pop(0)
			if name in subgraph or name not in modules:
				continue
			module = modules[name]
			outputs = ["out" if output == pre_rx else output for output in module.outputs]
			module = module._replace(outputs=outputs)
			subgraph[name] = module
			queue += outputs
		subgraphs.append(subgraph)
	return pre_rx, subgraphs

pre_rx, subgraphs = split_graph(modules)

assert modules[pre_rx].type == "&", "unexpected graph shape"
# Since pre_rx is a &, it sends a low pulse to rx when all its inputs are high.

"""
Each subgraph is of form:
	a -> b -> ... -> c
where all are flip-flops, plus a central &x which takes output from SOME of them
and sends input to SOME of them. Finally there's a &y which does nothing but invert x.
Since we want y's output to be high, we want x's output to be low. This happens when all
the flip-flops are high. But this also causes a to flip, so it's only ever high in the middle of
a press. So all subgraphs need it to happen at the same time.

Think of the chain of flip-flops as a binary counter. It counts presses (low inputs)
until it reaches all 1s in x-connected bits, at which point the x node adds 2^n
(for some n) for each node it's connected to.
"""

def analyze_subgraph(subgraph):
	# Validate graph shape

	# First node is a flip-flop
	initial = subgraph["in"].outputs
	assert len(initial) == 1
	initial = initial[0]
	assert subgraph[initial].type == "%"

	# Discover chain of flip-flops
	name = initial
	chain = []
	to_conj = []
	found_conj = set()
	while True:
		chain.append(name)
		out_ffs = [output for output in subgraph[name].outputs if subgraph[output].type == "%"]
		out_conj = [output for output in subgraph[name].outputs if subgraph[output].type == "&"]
		if out_conj:
			to_conj.append(name)
			found_conj.add(out_conj[0])
		if len(out_ffs) != 1:
			break
		name = out_ffs[0]

	# Assert they all connect to the same conj
	assert len(found_conj) == 1
	main_conj, = found_conj

	# Assert the main conj connects to one other, then out.
	not_conj = [output for output in subgraph[main_conj].outputs if subgraph[output].type == "&"]
	assert len(not_conj) == 1
	not_conj, = not_conj
	assert subgraph[not_conj].outputs == ["out"]

	# We should have now discovered all nodes
	assert set(chain) | {main_conj, not_conj, "in"} == set(subgraph)

	# Length of flip flop chain is the number of bits in counter.
	counter_size = 2**len(chain)

	# It matches when all the bits in to_conj are high
	match_at = sum(2**chain.index(name) for name in to_conj)

	# First element of counter has value 1, then 2, 4, etc. Determine total value
	# added upon match.
	match_adds = sum(2**chain.index(output) for output in subgraph[main_conj].outputs if output in chain)

	# We observe that the match_at value + the match_adds value always exactly causes the counter to reset.
	assert match_at + match_adds == counter_size
	# This means the loop period is just match_at.

	return counter_size, match_at

analyses = [analyze_subgraph(subgraph) for subgraph in subgraphs]
assert len(set(size for size, period in analyses)) == 1
# Since they're all the same size, they match up simply with LCM of the loop periods.
periods = [period for size, period in analyses]

print(math.lcm(*periods))
