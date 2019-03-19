nbLieux = int(input());

lieu= 0;
nbVilles = 0;
for lieu in range(nbLieux):
	nbHabitants = int(input());
	if nbHabitants > 10000:
		nbVilles +=1;

print(nbVilles);