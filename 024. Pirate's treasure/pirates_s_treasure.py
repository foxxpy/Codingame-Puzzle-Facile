import sys
import math

def check_if_treasure(treasure_map, i, j, w, h):
    """On regarde si la case envoyée est un trésor ou non. Si la case totalise un score de 8, c'est que c'est un trésor.
    Un spot hors de la carte ou valant 1 incrémente le score de 1"""
    score = 0
    
    #On regarde chaque case autour du spot
    for neighbor_spot in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
        if neighbor_spot[0] < 0 or neighbor_spot[0] > h-1 or neighbor_spot[1] < 0 or neighbor_spot[1] > w - 1:
            score += 1
        
        elif treasure_map[neighbor_spot[0]][neighbor_spot[1]] == "1":
            score += 1
    print("score : "+str(score), file=sys.stderr)
    
    if score == 8:
        return True
    else:
        return False
            
    
#Instanciation des variables
w = int(input())
h = int(input())
treasure_map = list()
treasure_found = False
x_treasure = 0
y_treasure = 0


#Récupération de la carte
for i in range(h):
    treasure_map.append(input().split())


#On parcourt la carte pour trouver le trésor
for i, line in enumerate(treasure_map):
    for j, spot in enumerate(line):
        treasure_Found = False
        
        #Si c'est un spot vide, on regarde ses alentours pour déterminer si c'est un trésor ou non
        if spot == "0":
            treasure_found = check_if_treasure(treasure_map, i, j, w, h)
            
            if treasure_found:
                x_treasure = j
                y_treasure = i

print(str(x_treasure)+" "+str(y_treasure))