nbMarchands = int(input());
marchand= 0;
galettes= [];

for marchand in range(nbMarchands):
	prixGalette= int(input());
	galettes.append(int(prixGalette));
	marchand+=1;

print(len(galettes) - galettes[-1::-1].index(min(galettes)))
