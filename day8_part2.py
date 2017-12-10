import sys

try:
	fname = sys.argv[1]
except:
	fname = 'day8.txt'

with open(fname, 'r') as f:
	instructions = [l.strip() for l in f.readlines()]

values = { k:0 for k in (i.split(' ')[0] for i in instructions) }

maxval = 0
for inst in instructions:
	inst = inst.split(' ')
		
	cond = values[inst[4]] > int(inst[6]) if inst[5] == '>' else \
	       values[inst[4]] >= int(inst[6]) if inst[5] == '>=' else \
	       values[inst[4]] == int(inst[6]) if inst[5] == '==' else \
	       values[inst[4]] <= int(inst[6]) if inst[5] == '<=' else \
	       values[inst[4]] < int(inst[6]) if inst[5] == '<' else \
	       values[inst[4]] != int(inst[6]) if inst[5] == '!=' else None
	
	if cond:
		if inst[1] == 'inc':
			values[inst[0]] += int(inst[2])
		elif inst[1] == 'dec':
			values[inst[0]] -= int(inst[2])
		
		if maxval < values[inst[0]]:
			maxval = values[inst[0]]

print(maxval)
	
	
