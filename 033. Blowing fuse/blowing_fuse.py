import sys
import math

#Instanciation des variables
n, m, c = [int(i) for i in input().split()]
list_device_consumption = list()
current_consumption = 0
fuse_was_blown = False
max_consumption = 0


#On récupère la consommation des appareils
for i, nx_consumption in enumerate(input().split()):
    nx_consumption = int(nx_consumption)
    list_device_consumption.append({"consumption" : nx_consumption, "status" : "OFF"})

#On récupère la séquence des interrupteurs qui sont activés/désactivés
for i, num_click in enumerate(input().split()):
    mx = int(num_click)

    #Si on appuie un nombre impair de fois sur l'interrupteur, alors il sera sur ON
    if list_device_consumption[mx-1]["status"] == "OFF":
        list_device_consumption[mx-1]["status"] = "ON"
        current_consumption += list_device_consumption[mx-1]["consumption"]

    else:
        list_device_consumption[mx-1]["status"] = "OFF"
        current_consumption -= list_device_consumption[mx-1]["consumption"]

    #Si la consommation actuelle de courant dépasse la capacité du fusible principal
    if current_consumption >= c:
        fuse_was_blown = True
        
    #Si la consommation de courant actuelle est supérieure à la consommation maximale de courant qu'a connu ce réseau électrique
    if current_consumption > max_consumption:
        max_consumption = current_consumption

#Résultat final
if fuse_was_blown:
    print("Fuse was blown.")

else:
    print("Fuse was not blown.")
    print("Maximal consumed current was "+str(max_consumption)+" A.")