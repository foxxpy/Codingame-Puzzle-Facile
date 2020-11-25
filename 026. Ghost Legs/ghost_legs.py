import sys
import math

#Instanciation des variables
w, h = [int(i) for i in input().split()]
list_lines = list()
list_start = list()

#On ajoute nos lignes à notre tableau de lignes
for i in range(h):
    line = input()
    list_lines.append(line)
    print(line, file=sys.stderr)

list_start = list_lines[0].split("  ")

#On cherche l'arrivée pour chaque point de départ
for start in list_start:
    index_start = list_lines[0].index(start)
    index_position = index_start
   
    for line in list_lines:
        #Si on a un tiret à gauche, on part à -3 sur la gauche
        if index_position - 1 > -1 and line[index_position-1] == "-":
            index_position -= 3
           
        #SI on a un tiret à droite, on part à +3 sur la droite
        elif index_position + 1 < w and line[index_position+1] == "-":
            index_position += 3
           
    #On affiche le point de départ et l'arrivée
    print(start+list_lines[h-1][index_position])