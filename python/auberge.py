age = int(input());
poidBagages= int(input());
prix = 0;
ageAubergiste= 60;
supBagages = 10;

if age == ageAubergiste:
	print(prix);

elif age < 10:
	print(prix+5);

elif age >= 10 and age != 60 and poidBagages >= 20:
	print((prix+30)+supBagages);

else:
	print(prix+30);
