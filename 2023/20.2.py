
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

def press():
	queue = [("button", "broadcaster", False)] # (source, dest, is_high)
	while queue:
		source, name, is_high = queue.pop(0)
		if name == "rx" and not is_high:
			return True
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
	return False

presses = 0
while not press():
	presses += 1
print presses
