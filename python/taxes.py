from math import*

oldTaxe= float(input())
newTaxe= float(input())
price= float(input())
htPrice= round(price,2)-(round(price,2)*(oldTaxe/100))
newPrice= round(htPrice,2) + (round(htPrice)*(newTaxe/100))
print(round(newPrice))
