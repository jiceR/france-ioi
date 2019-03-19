hauteurArbre= int(input());
folioles = int(input());

if hauteurArbre <= 5 and folioles >= 8:
	print("Tinuviel");

elif hauteurArbre <= 8 and folioles <= 5:
	print("Falarion"); 

elif hauteurArbre >= 10 and folioles >= 10:
	print("Calaelen"); 

elif hauteurArbre >= 12 and folioles <= 7:
	print("Dorthonion");  