grdBase= int(input());
ptBase= int(input());
aire= 0;
largeur= ptBase;

for loop in range(grdBase - ptBase+1):

	aire= aire+largeur*largeur;
	largeur+=1;


print(aire);

