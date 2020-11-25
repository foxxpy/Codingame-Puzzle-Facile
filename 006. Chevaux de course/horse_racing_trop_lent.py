import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
liste_des_chevaux = list()
plus_faible_ecart_entre_deux_puissances = 10000000

for i in range(n):
    pi = int(input())
    liste_des_chevaux.append(pi)
    
    
    if i > 0:
        for j in range(i):
            if abs(liste_des_chevaux[j] - pi) < plus_faible_ecart_entre_deux_puissances:
                plus_faible_ecart_entre_deux_puissances = abs(liste_des_chevaux[j] - pi)
        

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(plus_faible_ecart_entre_deux_puissances)