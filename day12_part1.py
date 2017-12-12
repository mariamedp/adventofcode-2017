import sys
from collections import defaultdict

try:
	fname = sys.argv[1]
except:
	fname = 'day12.txt'

with open(fname, 'r') as f:
	input = f.readlines()


connections = defaultdict(set)
for line in input:
	id, ids_con = line.strip().split(' <-> ')
	for id_con in ids_con.split(', '):
		connections[id].add(id_con)
		connections[id_con].add(id)

group = set()
to_visit = ['0']
while to_visit:
	id = to_visit.pop()
	group.add(id)
	to_visit += [id_con for id_con in connections[id] if id_con not in group]

print(len(group))
