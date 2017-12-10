import sys

try:
	fname = sys.argv[1]
except:
	fname = 'day6.txt'

with open(fname, 'r') as f:
	blocks = [int(n) for l in f.readlines() for n in l.split()]

n = 0
states_seen = []
while True:
	n += 1
	
	ind, val = max(enumerate(blocks), key = lambda x: x[1])
	blocks[ind] = 0
	redist = int(val / len(blocks))
	blocks = [b + redist for b in blocks]
	redist = val - redist*len(blocks)
	for i in range(1, redist+1):
		blocks[(ind + i) % len(blocks)] += 1
	
	state = ''.join([str(b) for b in blocks])
	if state in states_seen:
		break
	else:
		states_seen.append(state)

print(len(states_seen) - states_seen.index(state))
