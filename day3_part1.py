import sys

try:
	input = int(sys.argv[1])
except:
	input = 312051


axis_spiral = [1]
step = 1
neqsteps = 1
while input > axis_spiral[-1]:
	axis_spiral.append(axis_spiral[-1] + step)
	if step % 2 == 1:
		step += 1
	elif neqsteps == 3:
		step += 1
		neqsteps = 1
	else:
		neqsteps += 1

axis_spiral.remove(1)


dist_sp1 = input - axis_spiral[-2]
dist_sp2 = axis_spiral[-1] - input

if dist_sp1 < dist_sp2:
	axis_spiral.pop()
	dist_dir2 = dist_sp1
else:
	dist_dir2 = dist_sp2

steps_dir1 = int((len(axis_spiral) - 1) / 4) + 1

print(steps_dir1 + dist_dir2)
