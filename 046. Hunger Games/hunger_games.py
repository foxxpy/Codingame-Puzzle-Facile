import sys
import math

#Instanciation des variables
n = int(input())
tributes = dict()

#Récupération des tributs
for i in range(n):
    player_name = input()
    tributes[player_name] = {"Killed" : [], "Killer" : ""}

#On associe les tueurs aux tués et inversement
turns = int(input())
for i in range(turns):
    info = input().split(" killed ")
    killed = info[1].split(", ")
    tributes[info[0]]["Killed"] += killed
    for kill in killed:
        tributes[kill]["Killer"] = info[0]

#On cherche le gagnant
for key, value in tributes.items():
    if value["Killer"] == "":
        value["Killer"] = "Winner"
i = 1

#On affiche les résultats par ordre alphabétique, et les tributs tués par ordre alphabétique également
for key in sorted(tributes.keys()):
    killed = "None" if len(tributes[key]["Killed"]) == 0 else ", ".join(sorted(tributes[key]["Killed"]))
    print("Name:", key)
    print("Killed:", killed)
    print("Killer:", tributes[key]["Killer"])
    
    if i < len(tributes.keys()):
        print()
    i = i + 1
