import sys
import math


#Instanciation des variables
size = int(input())
angle = int(input())
indice = 0
begin, end, step = 0, size * 2 - 1, 1
angle_modulo = (angle//45) % 8
losange = dict()

#On récupère le bloc initial et on le pivote de 90, 180, 270, 0 degré
for i in range(size):
    line = input().replace(" ", "")

    for j, char in enumerate(line):
        if angle_modulo == 1:
            indice=i+size-1-j

        elif angle_modulo == 3:
            indice = i+j
            begin, end, step = 2 * size - 2, -1, -1

        elif angle_modulo == 5:
            indice = i+size-1+j
            begin, end, step = 2*size - 2, -1, -1

        else:
            indice = i + j

        if indice in losange.keys():
            losange[indice].append(char)
        else:
            losange[indice] = [char]

print(losange, file=sys.stderr)

#On établit les paramètres d'affichage du losange
space = size
down = True

if angle_modulo == 7:
    for key in losange.keys():
        losange[key] = losange[key][::-1]

#On affiche le losange
for i in range(begin, end, step):
    if down:
        space -= 1
    else:
        space += 1
    print(" "*space, end="")
    for j, char in enumerate(losange[i]):
        print(char, end="")
        if j < len(losange[i])-1:
            print(" ",end="")
    print(" "*space, end="")
    print()

    #Si le nombre d'espace au début atteint 0, on le réincrémentera ensuite
    if space == 0:
        down = False
