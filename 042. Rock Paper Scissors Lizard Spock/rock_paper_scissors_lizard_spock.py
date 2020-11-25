import sys
import math

def duel(tournament, i, rules):
    sign_player_1 = tournament[i]["sign"]
    sign_player_2 = tournament[i+1]["sign"]
    loser = None
    
    #Si le joueur 2 bat le joueur 1 ou qu'il y'a égalité et que le numéro du joueur 2 est plus faible
    if sign_player_1 in rules[sign_player_2] or \
    (not sign_player_1 in rules[sign_player_2] and not sign_player_2 in rules[sign_player_1] and tournament[i+1]["numplayer"] < tournament[i]["numplayer"]):
        print("Player 2 wins", file=sys.stderr)
        tournament[i+1]["beat"].append(str(tournament[i]["numplayer"]))
        loser = i
        
    #Si le joueur 1 bat le joueur 2 ou qu'il y'a égalité et que le numéro du joueur 1 est plus faible
    elif sign_player_2 in rules[sign_player_1] or \
    (not sign_player_1 in rules[sign_player_2] and not sign_player_2 in rules[sign_player_1] and tournament[i]["numplayer"] < tournament[i+1]["numplayer"]):
        print("Player 1 wins", file=sys.stderr)
        tournament[i]["beat"].append(str(tournament[i+1]["numplayer"]))
        loser = i+1
    
    return tournament, loser
        


#Instanciation des variables
n = int(input())
tournament = []
rules = { #Indique pour chaque signe, les signes qu'il bat
    "C" : ["P", "L"],
    "P" : ["R", "S"],
    "R" : ["L", "C"],
    "L" : ["S", "P"],
    "S" : ["C", "R"]
}

#On récupère les informations des joueurs
for i in range(n):
    numplayer, signplayer = input().split()
    numplayer = int(numplayer)
    player = { 
        "numplayer" : numplayer,
        "sign" : signplayer,
        "beat" : [],
        "loser" : False
    }
    tournament.append(player)
    

#On organise le tournoi
while(len(tournament) > 1):
    loser = []
    for i in range(0, len(tournament), 2):
        loses_duel = 0
        tournament, loses_duel = duel(tournament, i, rules)
        loser.append(loses_duel)

    #On la parcourt en sens inverse pour ne pas déranger l'ordre des index de la liste tournament
    for i in loser[::-1]:
        tournament.pop(i)

#On affiche le gagnant et sur la seconde ligne, ceux qu'il a vaincu
print(tournament[0]["numplayer"])
print(" ".join(tournament[0]["beat"]))