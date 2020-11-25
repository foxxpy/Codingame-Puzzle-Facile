import sys
import math

#Instanciation des variables et état initial du jeu
op_bowls = [int(x) for x in input().split(" ")]
my_bowls = [int(x) for x in input().split(" ")]
num = int(input())
replay = False
num_grain = my_bowls[num]
my_bowls[num] = 0

#Tours de jeu
i = num+1
my_bowl = True
endLine = len(my_bowls) - 1

while(num_grain>0):
    #On regarde si on doit remplir les bols de l'adversaire ou les nôtres
    if my_bowl:
        my_bowls[i] += 1
    else:
        op_bowls[i] += 1
        
    #Si on atteint la fin d'une ligne de bols d'un joueur, on remplit les bols de l'autre joueur
    if i == endLine:
        i = 0
        my_bowl = True if my_bowl == False else False
        endLine = len(my_bowls)-1 if my_bowl else len(my_bowls) - 2 #On ne peut ajouter un grain sur la réserve de l'adversaire
    else:
        i = i + 1
        
    num_grain -= 1
    
    #Conditions nous autorisant à rejouer si elles sont vraies : on n'a plus de grain, on est le premier bol de l'adversaire
    if num_grain == 0 and not my_bowl and i == 0:
        replay = True

op_bowls = [str(x) for x in op_bowls]
my_bowls = [str(x) for x in my_bowls]
print(" ".join(op_bowls[:-1]), "["+op_bowls[-1]+"]")
print(" ".join(my_bowls[:-1]), "["+my_bowls[-1]+"]")
if replay:
    print("REPLAY")