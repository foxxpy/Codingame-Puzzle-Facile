import sys
import math

class Robot:
    def __init__(self, pos, status):
        self.pos = pos
        self.status = status

#Instanciation des variables
w, h = [int(i) for i in input().split()]
n = int(input())
lines = []
rob = None
right = {
    "UP" : "RIGHT",
    "RIGHT" : "DOWN",
    "DOWN" : "LEFT",
    "LEFT" : "UP"
}

next_pos = {
    "UP" : (-1, 0),
    "RIGHT" : (0, 1),
    "DOWN" : (1, 0),
    "LEFT" : (0, -1)
}

position_visited = dict()
total_move = 0
cycle = False
move = 0

#On récupère les informations du circuit et la position du robot
for i in range(h):
    line = input()
    print(line, file=sys.stderr)
    lines.append(line)
    if "O" in line:
        rob = Robot((i, line.index("O")), "UP")
        position_visited[(i, line.index("O"), "UP")] = 0

#Tant qu'on est pas dans un cycle ou que le nombre de mouvements n'a pas atteint le nombre n
while(not cycle and move < n):
    move += 1
    next_position = tuple(map(sum, zip(rob.pos, next_pos[rob.status])))

    #Si à la prochaine position on tombe sur un mur, on tourne le robot dans le sens anti-horaire
    while(lines[next_position[0]][next_position[1]] == "#"):
        rob.status = right[rob.status]
        next_position = tuple(map(sum, zip(rob.pos, next_pos[rob.status])))

    #Si la position n'a pas déjà été visitée, on l'ajoute au dictionnaire des positions visitées
    if not (next_position[0], next_position[1], rob.status) in position_visited.keys():
        position_visited[(next_position[0], next_position[1], rob.status)] = move

    #Sinon c'est qu'on est dans un cycle et on calcule le nombre total de mouvement
    #auquel on soustrait le numéro de la case du cycle sur laquelle est le robot actuellement
    else:
        cycle = True
        total_move = move - position_visited[(next_position[0], next_position[1], rob.status)]

    rob.pos = next_position

#Si le robot a été pris dans un cycle, le numéro de la position de chaque case du cycle
#est équivalent au n-ième mouvement divisé par le nombre total de mouvements
if cycle:
    position = n % total_move
    for key, value in position_visited.items():
        if position == value:
            print(key[1], key[0])
else:
    print(rob.pos[1], rob.pos[0])