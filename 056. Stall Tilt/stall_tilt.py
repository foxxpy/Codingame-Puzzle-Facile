import sys
import math

#Instanciation des variables
n = int(input())
v = int(input())
speeds = list()
motos = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
leaderboard = list()
max_speed = 60


#On ajoute les vitesses des motos à la liste "speeds"
for i in range(n):
    speed = int(input())
    speeds.append((motos[i], speed))

for i in range(v):
    r = int(input())
    max_speed_bend = math.floor(math.sqrt(math.tan(math.radians(60)) * r * 9.81))

    #Si la vitesse maximale pour passer ce virage est inférieure aux vitesses maximales des anciens virages
    #On la garde en mémoire, ce sera notre indicateur pour la vitesse maximale de la moto
    if max_speed_bend < max_speed:
        max_speed = max_speed_bend

    temp = list()

    #Si la vitesse d'une moto est supérieure à la vitesse à laquelle le virage est passable sans tomber
    #Alors on l'ajoute à temp (la moto est tombée)
    for moto in speeds:
        if moto[1] > max_speed_bend:
            temp.append(moto)

    for moto in temp:
        speeds.remove(moto)

    #On trie les motos tombées à chaque virage de la plus rapide à la plus lente
    leaderboard = sorted(temp, key=lambda t: t[1], reverse=True) + leaderboard

leaderboard = sorted(speeds, key=lambda t : t[1], reverse=True) + leaderboard

#Affichage du résultat final
print(max_speed)
print("y")
for moto in leaderboard:
    print(moto[0])
