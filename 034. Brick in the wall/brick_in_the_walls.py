import sys
import math


def calculate_amount_of_work(L, m, g=10):
    amount_of_work = float(((L-1) *6.5/100) * g * m)

    return amount_of_work


#Instanciation des variables
x = int(input())
n = int(input())
L = 1
nb_bricks_on_line = 0
list_of_m = list()
minimum_work = 0.0


#Récupération des briques
for i in input().split():
    m = int(i)
    list_of_m.append(m)


#On trie les briques de la plus lourde à la plus légère
list_of_m.sort(reverse=True)

#On pose autant de briques que l'on peut par ligne, dés qu'on a fini une ligne, on passe à la suivante
while len(list_of_m) > 0:
    minimum_work += calculate_amount_of_work(L, list_of_m[0])
    list_of_m.pop(0)
    nb_bricks_on_line += 1
    if nb_bricks_on_line == x:
        L = L + 1
        nb_bricks_on_line = 0

#Résultat final
print(format(minimum_work, ".3f"))
