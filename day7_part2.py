import sys

try:
	fname = sys.argv[1]
except:
	fname = 'day7.txt'

with open(fname, 'r') as f:
	file_lines = [l.strip() for l in f.readlines()]

weights = {l.split(' ')[0]:int(l.split(' ')[1][1:-1]) for l in file_lines}
parents = {l.split(' ')[0]:[w.strip() for w in l.split('>')[1].split(',')] for l in file_lines if '->' in l}
leaves = {k:v for k,v in weights.items() if k not in parents.keys()}

found = False
while not found:
	for k,v in parents.items():
		if k not in leaves:
			node_weights = [leaves.get(w, None) for w in v]
			if not all(node_weights):
				continue
			if len(set(node_weights)) > 1:
				for wrong_weight in set(node_weights):
					if node_weights.count(wrong_weight) == 1:
						break
				ind_error = node_weights.index(wrong_weight)
				correct_weight = (set(node_weights) - set([wrong_weight])).pop()
				dif = wrong_weight - correct_weight
				print(weights[v[ind_error]] - dif)
				found = True
				break
			else:
				leaves[k] = sum(node_weights) + weights[k]

