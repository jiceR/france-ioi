personId = int(input());
listLength = int(input());
listeId = [];

for loop in range(listLength):
	number= int(input());
	listeId.append(int(number));

if personId in listeId:
	print("Sorti de la ville");
else:
	print("Encore dans la ville");
