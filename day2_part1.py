import sys

try:
	fname = sys.argv[1]
except:
	fname = 'day2.txt'

with open(fname, 'r') as f:
	spreadsheet = [[int(n) for n in l.split()] for l in f.readlines()]

checksum = 0
for line in spreadsheet:
	checksum += (max(line) - min(line))

print(checksum)
