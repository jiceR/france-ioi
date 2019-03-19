nbKarvas = int(input());
karvas= 0;

for loop in range(nbKarvas):

	poidKarvas= int(input("poid du karvas: "));
	ageKarvas= int(input("age du karvas: "));
	corneKarvas= int(input("cornes du karvas: "));
	tailleKarvas= int(input("taille du karvas: "));
	noteKarvas= (corneKarvas*tailleKarvas)+poidKarvas;
	karvas+=1;

	print(noteKarvas);
