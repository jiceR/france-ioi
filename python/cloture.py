nbmaison= int(input());
maison = 0;
ordonnees = [];
absisses = [];

for maison in range(nbmaison):
	x= int(input());
	ordonnees.append(int(x));
	y= int(input());
	absisses.append(int(y));

longueurX= max(ordonnees) - min(ordonnees);
hauteurY= max(absisses) - min(absisses);
perimetre= (longueurX*2)+(hauteurY*2);

print(perimetre);