pairesZones = int(input());
zone = 0;



for zone in range(pairesZones):

	xMin1= int(input())
	xMax1= int(input())
	yMin1= int(input())
	yMax1= int(input())

	xMin2= int(input())	
	xMax2= int(input())
	yMin2= int(input())
	yMax2= int(input())
	zone+=1;

	if (xMin2 < xMax1 and yMin2 > yMin1) or (ymin2 < yMin1 and xMin2 > xMin1) :
		print("OUI")

	else:
		print("NON")



