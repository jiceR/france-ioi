nbpersonnes = int(input());
probabilite = 0


for loop in range (nbpersonnes):
	taille = int(input());
	if taille >= 178 and taille <= 182:
		probabilite+=1
	age = int(input());
	if age >= 34:
		probabilite+=1
	poid = int(input());
	if poid < 70:
		probabilite+=1
	cheval = int(input());
	if not cheval:
		probabilite+=1
	cheveux = int(input());
	if cheveux:
		probabilite+=1

	if probabilite == 5:
		print("Très probable")
	elif probabilite >= 3 and probabilite <= 4:
		print("Probable")
	elif probabilite >0 and probabilite <=2:
		print("Peu probable")
	else: 
		print("Impossible")
	print(probabilite)

	probabilite= 0;
	