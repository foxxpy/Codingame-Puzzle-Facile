import sys
import math

def river(r):
    """Calcul du nombre suivant selon les conditions de l'énoncé.
    Valeur du nombre + la somme des chiffres qui le composent"""
    
    return r+sum(int(x) for x in str(r))

#Instanciation des variables
r_1 = int(input())
can_be_a_meeting_point = "NO"

#On cherche UN et UN SEUL nombre qui pourrait croiser r_1
for i in range(1, r_1):
    r = river(i)
    if r == r_1:
        can_be_a_meeting_point = "YES"
        break

print(can_be_a_meeting_point)
