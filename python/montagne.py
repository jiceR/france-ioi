nbMonteeDescente = int(input());
montee= [];
descente = [];

for loop in range(nbMonteeDescente):
	denivelee= int(input());
	if denivelee >= 0:
		montee.append(int(denivelee));
	else:
		descente.append(int(denivelee));

print(sum(montee));
print(-sum(descente));


