import sys
import math

#Instanciation des variables
lines = list()
elements = [ [], [], [], [], [] ]
win = False

#On nous donne les lignes
for i in range(3):
    line = input()
    
    #On regarde si on peut déjà gagner avec les lignes
    if line.count("O") == 2 and "." in line:
        line = "OOO"
        win = True
    lines.append(line)
        
    #Si on a pas déjà gagné, on ajoute les colonnes et les diagonales
    if not win:
        elements[0].append(line[0]) #colonne 0
        elements[1].append(line[1]) #colonne 1
        elements[2].append(line[2]) #colonne 2
        elements[3].append(line[i]) #diagonale 0
        elements[4].append(line[3-i-1]) #diagonale 1


#On analyse des colonnes et des diagonales
if not win:
    for i, col in enumerate(elements):
        if col.count("O") == 2 and "." in col:
            index_point = col.index(".")
            i = index_point if i==3 else i 
            i = 3 - index_point - 1 if i==4 else i 
            lines[index_point] = lines[index_point][:i]+"O"+lines[index_point][i+1:]
            win = True
            break
        
#Si on a gagné
if win:
    for line in lines:
        print(line)
        
#Si on a perdu
else:
    print("false")