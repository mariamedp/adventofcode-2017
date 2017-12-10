import sys

try:
	fname = sys.argv[1]
except:
	fname = 'day4.txt'

with open(fname, 'r') as f:
	passphrases = [l.split() for l in f.readlines()]

nvalid = 0
for passph in passphrases:
	if len(passph) == len(set(passph)):
		nvalid += 1

print(nvalid)
