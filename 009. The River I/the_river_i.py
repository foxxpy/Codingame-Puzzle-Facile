import sys
import math


def river(r):
    """Calcul du nombre suivant selon les conditions de l'énoncé.
    Valeur du nombre + la somme des chiffres qui le composent"""
    
    list_of_number_in_r = list(str(r)) #liste des chiffres dans r
    list_of_number_in_r = [int(x) for x in list_of_number_in_r] #conversion en int de la liste des chiffres
    sum_of_number_in_r = sum(list_of_number_in_r) #calcul de la somme
    
    return r+sum_of_number_in_r



#Instanciation des variables
r_1 = int(input())
r_2 = int(input())

#Tant que r_1 et r_2 ne sont pas égaux, on continue de les faire croître
while(r_1 != r_2):
    if r_1 < r_2:
        r_1 = river(r_1)
    else:
        r_2 = river(r_2)

print(r_1)
