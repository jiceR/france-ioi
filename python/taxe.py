dé1= int(input());
dé2= int(input());

somme= dé1 + dé2;

if somme >= 10:
	print("Taxe spéciale !");
	print("36");

else:
	print("Taxe regulière");
	print(somme*2);