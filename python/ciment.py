from math import*
ciment = float(input());
sac= 60
if ciment%sac > 0:
	print(ceil(ciment/sac)*45)
else:
	print(int((ciment/60)*45))


