import sys

try:
	fname = sys.argv[1]
except:
	fname = 'day2.txt'

with open(fname, 'r') as f:
	spreadsheet = [[int(n) for n in l.split()] for l in f.readlines()]

checksum = 0
for line in spreadsheet:
	line.sort(reverse=True)
	found = False
	for i in range(len(line)):
		for j in range(i+1, len(line)):
			if line[i] % line[j] == 0:
				checksum += (line[i] / line[j])
				found = True
				break
		if found:
			break

print(checksum)
