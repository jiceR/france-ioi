mois = int(input());
mois29jours = 29
mois30jours = 30;
mois31jours = 31

if mois == 1 or mois == 2 or mois ==3 or mois== 7 or mois == 8 or mois== 9:
	print(mois30jours)

elif mois == 4 or mois == 5 or mois ==6 or mois== 10:
	print(mois31jours)

elif mois == 11:
	print(mois29jours)