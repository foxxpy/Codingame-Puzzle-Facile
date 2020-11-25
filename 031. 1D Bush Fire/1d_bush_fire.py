import sys
import math

n = int(input())
number_of_water_drops = int()

for i in range(n):
    line = input()
    list_position_fire = list()
    number_of_water_drops = 0
    j = 0
   
    #On parcourt la ligne pour récupérer la position de tous les feux
    for position, char in enumerate(line):
        if char == "f":
            list_position_fire.append(position)
           
    #On parcourt notre liste de position des feux pour éteindre un maximum de feux avec un jet d'eau
    while(j < len(list_position_fire)):

        #Si les feux sont à deux cases de distance : on incrémente j de 2 
	#pour pas compter une deuxième fois le feu suivant
        if j < len(list_position_fire) - 1 and list_position_fire[j+1] - list_position_fire[j] == 2:
            j = j + 2
           
        #Si la distance entre le feu étudié et le feu suivant est de 1, 
	#on regarde si il n'y a pas un troisième feu qui est à une distance de 1 du deuxième            
        elif j < len(list_position_fire) - 1 and list_position_fire[j+1] - list_position_fire[j] == 1:
           
            #Si un troisième feu est à une distance de 1 du deuxième
            if j+2 < len(list_position_fire) and list_position_fire[j+2] - list_position_fire[j+1] == 1:
                j = j + 3
           
            #Sinon cela veut dire qu'on a seulement 2 feux côte-à-côte
            else:
                j = j + 2
        #Si aucun feu n'est à une distance de 1 ou de 2 du feu étudié
        else:
            j = j + 1
           
        number_of_water_drops += 1
               
    print(number_of_water_drops)