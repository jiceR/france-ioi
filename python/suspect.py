dateDebut= int(input())
dateFin= int(input())
nbInvites= int(input())
suspect = 0

for loop in range(nbInvites):
	entreeInvite= int(input())
	sortieInvite= int(input())
	if entreeInvite<= dateFin and sortieInvite >= dateDebut:
		suspect+=1

print(suspect)