import sys
import math


n = int(input())
triforce = list()

#Boucle dans laquelle on créé le triangle
for i in range(n):
    triangle = "*"*(2*i+1)
    triforce.append(triangle)

#Instanciation des variables calculant le nombre d'espaces entre les triangles de la triforce
space = 2*(n-1)+1
inter_space = space
start_space = space

#Affichage de la triforce
for i in range(2):
    for j, star in enumerate(triforce):
        line = ""
        #Si on est à la toute première ligne, on affiche le point (.). Sinon on affiche la ligne correspondante
        if i == 0 and j == 0:
            line += "."+" "*(start_space-1)+star
        else:
            line += " "*start_space+star
            
        #On affiche le second triangle sur la ligne avec le bon inter-espace
        if i == 1:
            line += " "*inter_space+star
            inter_space -= 2
        start_space -= 1

            
        print(line)
