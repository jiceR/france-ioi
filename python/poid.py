membresTeams= int(input());
poidTotalTeam1 = 0;
poidTotalTeam2 = 0;
membre= 0;

for membre in range(membresTeams):
	poidMemmbreTeam1= int(input());
	poidTotalTeam1 += poidMemmbreTeam1;
	poidMemmbreTeam2= int(input());
	poidTotalTeam2 += poidMemmbreTeam2;

if poidTotalTeam1 > poidTotalTeam2:
	print("L'équipe 1 a un avantage")
	print("Poids total pour l'équipe 1 :",poidTotalTeam1);
	print("Poids total pour l'équipe 2 :",poidTotalTeam2);

else:
	print("L'équipe 2 a un avantage")
	print("Poids total pour l'équipe 1 :",poidTotalTeam1);
	print("Poids total pour l'équipe 2 :",poidTotalTeam2);

