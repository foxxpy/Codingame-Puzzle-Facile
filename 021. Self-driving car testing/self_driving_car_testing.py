import sys
import math


#Instanciation des variables
n = int(input())
xthen_commands = input().split(";") #Instruction concernant les déplacements de la voiture
pos_car = int(xthen_commands[0])-1
del xthen_commands[0]
repeat = 0
direction = str()

for i in range(n):
    rthen_roadpattern = input().split(";")
    
    for j in range(int(rthen_roadpattern[0])):
        repeat = int(xthen_commands[0][:-1])

        if len(xthen_commands) > 0:
            direction = xthen_commands[0][len(xthen_commands[0])-1]
        
        if direction == "R":
            pos_car += 1
        elif direction == "L":
            pos_car -= 1
            
        xthen_commands[0] = xthen_commands[0].replace(str(repeat), str(repeat-1))
        
        #Si on finit d'appliquer la répétition d'une même instruction dans xthen_commands, on passe à l'instruction suivante en supprimant l'instruction actuelle
        #stockée à l'indice 0 de xthen_commands
        if repeat == 1:
            del xthen_commands[0]
        
        #On affiche la route et si on tombe sur la position de la voiture, on affiche un #
        for k in range(0, len(rthen_roadpattern[1])):
            if k == pos_car:
                print("#", end="")
            else:
                print(rthen_roadpattern[1][k], end="")
        
        #Passage à la ligne suivant 
        print()
            
