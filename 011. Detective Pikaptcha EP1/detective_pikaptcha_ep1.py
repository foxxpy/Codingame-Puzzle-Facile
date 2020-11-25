import sys
import math


def calcul_nb_case_adjacente(grille, coord, hauteur, largeur):
    i = coord[0]
    j = coord[1]
    nb_case_adjacente = 0

    #Test pour la case au-dessus
    if i > 0 and grille[i-1][j] == "0":
        nb_case_adjacente += 1

    #Test pour la case en-dessous
    if i < hauteur - 1 and grille[i+1][j] == "0":
        nb_case_adjacente += 1

    #Test pour la case à gauche
    if j > 0 and grille[i][j-1] == "0":
        nb_case_adjacente += 1

    #Test pour la case à droite
    if j < largeur-1 and grille[i][j+1] == "0":
        nb_case_adjacente += 1

    return nb_case_adjacente
        

#Instanciation des variables
largeur, hauteur = [int(i) for i in input().split()]
grille = list()

#On récupère les lignes dans notre grille
for i in range(hauteur):
    ligne = input()
    grille.append(ligne)

    
#On parcourt les lignes
for i in range(hauteur):
    #On parcourt les colonnes
    for j in range(largeur):
        nb_case_adjacente = 0
        coordonnees = (i,j)
        
        #Si on est sur un mur (case : "#")
        if grille[i][j] == "#":
            print("#", end="")
            
        #Si on est sur une case vide (case : "0")
        else:
            nb_case_adjacente += calcul_nb_case_adjacente(grille, coordonnees, hauteur, largeur)
            print(str(nb_case_adjacente), end="")
            
    #Saut de ligne du print final
    print()