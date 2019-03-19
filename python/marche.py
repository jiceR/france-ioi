nbJourMarche = int(input());
jour = 0;
distances = [];

for jour in range(nbJourMarche):
   distanceJour= input();
   distances.append(int(distanceJour));
   jour+=1;

print(max(distances));