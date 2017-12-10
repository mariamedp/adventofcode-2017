import sys

try:
	fname = sys.argv[1]
except:
	fname = 'day5.txt'

with open(fname, 'r') as f:
	steps = [int(n) for n in f.readlines()]

i = 0
n = 0
while 0 <= i < len(steps):
	step = steps[i]
	steps[i] += 1
	i += step
	n += 1

print(n)
