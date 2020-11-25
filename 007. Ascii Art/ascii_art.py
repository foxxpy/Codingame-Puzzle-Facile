import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def recherche_valeur_decimale_alphabet(t):
    """Création d'une liste contenant la place dans l'alphabet de chaque lettre du mot envoyé par Codingame"""
    L = [x for x in range(65,91)] #valeur des lettres majuscules dans la table ASCII
    liste_place_alphabet = list()
    
    for letter in t:
        #Si la lettre est comprise entre [A-Z]
        if ord(letter.upper()) in L:
            liste_place_alphabet.append(L.index(ord(letter.upper())))
        
        #Sinon on affiche le point d'interrogation
        else:
            liste_place_alphabet.append(26)
            
        
    return liste_place_alphabet

l = int(input())
h = int(input())
t = input()
liste_place_alphabet = recherche_valeur_decimale_alphabet(t)
answer = ""

for i in range(h):
    row = input()
    answer=""
    for letter in liste_place_alphabet:
        #On affiche la lettre en ASCII à partir de sa position dans row et de la largeur de la lettre en ASCII
        answer += row[letter*l:letter*l+l]
    
    print(answer)