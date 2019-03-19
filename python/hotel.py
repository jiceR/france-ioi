heureArrivee= int(input());
prixChambreBase= 10 ;
prixChambrePlus= prixChambreBase +(5*heureArrivee);
prixChambreMax= 53;

if prixChambrePlus >10 and prixChambrePlus< 53:
	print(prixChambrePlus);

elif heureArrivee == 0 :
	print(prixChambreBase);

elif heureArrivee == 12:
	print(prixChambreMax);

else:
	print(prixChambreMax);

