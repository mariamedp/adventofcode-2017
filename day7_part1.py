import sys

try:
	fname = sys.argv[1]
except:
	fname = 'day7.txt'

with open(fname, 'r') as f:
	trees = [l for l in f.readlines() if '->' in l]

roots = [l.split(' ')[0] for l in trees]
leaves = [w.strip() for l in trees for w in l.split('>')[1].split(',')]

print(set(roots) - set(leaves))
