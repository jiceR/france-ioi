nbMembresTeam = 3;

poidTeam1= int(input());
poidTeam2= int(input());
poidTeam1_2= int(input());
poidTeam2_2= int(input());
poidTeam1_3= int(input());
poidTeam2_3= int(input());

poidTotalTeam1= poidTeam1 + poidTeam1_2 + poidTeam1_3;
poidTotalTeam2= poidTeam2 + poidTeam2_2 + poidTeam2_3;

if poidTotalTeam1 > poidTotalTeam2:
	print("L'équipe 1 a un avantage")
	print("Poids total pour l'équipe 1 :", poidTotalTeam1);
	print("Poids total pour l'équipe 2 :", poidTotalTeam2);

else:
	print("L'équipe 2 a un avantage")
	print("Poids total pour l'équipe 2 :", poidTotalTeam2);
	print("Poids total pour l'équipe 1 :", poidTotalTeam1);

poidTotalTeam1 = 10
poidMemmbreTeam1= 20

poidTotalTeam1 += poidMemmbreTeam1

print(poidTotalTeam1)