dateEntree = int(input());
dateSortie = int(input());
nbPersonnes = int(input());
personne = 0;
suspect = 0;

for personne in range(nbPersonnes):
	dateArrivee= int(input());
	if dateArrivee >= dateEntree and dateArrivee <= dateSortie:
		suspect+=1;


print(suspect);		