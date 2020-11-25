import sys
import math

#Instanciation des variables
a1 = int(input())
n = int(input())
number_position = dict()
old_a1 = 0

for i in range(n-1):
    #Si on a jamais rencontré le nombre, le prochain terme est 0
    if not a1 in number_position.keys():
        number_position[a1] = i
        a1 = 0
    #Sinon le prochain terme est la position actuelle moins l'ancienne position du terme déjà rencontré
    else:
        old_a1 = number_position[a1]
        number_position[a1] = i
        a1 = i - old_a1

print(a1)
