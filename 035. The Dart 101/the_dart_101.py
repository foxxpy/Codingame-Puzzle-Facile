import sys
import math

#Instanciation des variables
n = int(input())
winner = str()
best_num_round = 100
list_of_players = list()

#Boucle donnant les noms des joueurs
for i in range(n):
    player = input()
    list_of_players.append(player)
    print(player, file=sys.stderr)
    
#Boucle de jeu
for i in range(n):
    shoots = input().split(" ")
    num_round = 1
    num_miss = 0
    actual_score = 0
    
    print(shoots, file=sys.stderr)
    j = 0
    
    #On parcourt le jeu de chaque joueur
    for shoot in shoots:
        
        #Tous les trois tirs, on passe au round suivant, on remet à zéro le nombre de tirs ratés, et on garde le score du round précédent
        #en mémoire dans actual_score_temp
        if j % 3 == 0:
            num_round += 1
            num_miss = 0
            actual_score_temp = actual_score
        
        #Si le joueur rate son tir
        if shoot == "X":
            num_miss += 1
            j = j + 1
            
            if num_miss == 1:
                actual_score = 0 if actual_score - 20 < 0 else actual_score - 20
            
            elif num_miss == 2:
                actual_score = 0 if actual_score - 30 < 0 else actual_score - 30
                
            else:
                num_miss = 0
                actual_score = 0
        
        #Si le joueur a réussi son tir, on remet à zéro son compteur de tirs ratés et on analyse son score   
        else:
            num_miss = 0
            
            #Si on trouve un * dans le tir, c'est qu'on doit opérer à une multiplication, sinon on ajoute simplement le score du tir
            if "*" in shoot:
                calcul = shoot.split("*")
                actual_score += int(calcul[0]) * int(calcul[1])
                
            else:
                actual_score += int(shoot)
                
            #Si le score actuel dépasse 101, on revient au score précédent
            if actual_score > 101:
                actual_score = actual_score_temp
                num_round += 1
                j = 0
                
            elif actual_score == 101 and num_round < best_num_round:
                best_num_round = num_round
                winner = list_of_players[i]
                
            else:
                j = j + 1

#Affichage du gagnant
print(winner)